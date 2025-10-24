import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    search_tool = DuckDuckGoSearchRun()
except Exception as e:
    print(f"Loi khi khoi tao LLM hoac Search Tool: {e}")
    print("Vui long kiem tra API key va cac thu vien da cai dat.")
    exit()

# ----- NODE 1: AGENT RESEARCHER -----
def researcher_node(state):
    """
    Agent nay nhan chu de (topic) tu state,
    dung search_tool de tim kiem, va tra ve ket qua nghien cuu (research).
    """
    print("--- Node: Researcher (Dang nghien cuu) ---")
    topic = state['topic']
    research_result = search_tool.run(topic)
    return {"research": research_result}


# ----- NODE 2: AGENT WRITER -----
def writer_node(state):
    """
    Agent nay nhan thong tin va VIET LAI neu bi phe binh.
    """
    print("--- Node: Writer (Dang viet bai) ---")
    topic = state['topic']
    research = state['research']
    critique = state.get('critique')

    if not critique:
        prompt_template = ChatPromptTemplate.from_template(
            "Ban la mot blogger chuyen nghiep. Dua tren thong tin nghien cuu sau, "
            "hay viet mot bai blog ngan (khoang 150-200 tu) ve chu de: {topic}.\n\n"
            "QUAN TRONG: Chi viet van ban thuan tuy (plain text). "
            "KHONG su dung bat ky dinh dang Markdown nao (vi du: khong dung ** , ## , * , - ).\n\n"
            "Thong tin nghien cuu:\n{research}"
        )
    else:
        print("--- Node: Writer (Bi che! Dang viet lai...) ---")
        prompt_template = ChatPromptTemplate.from_template(
            "Ban la mot blogger chuyen nghiep. Ban nhap truoc cua ban da bi phe binh. "
            "Dua tren nhan xet sau, hay viet lai bai blog cho tot hon.\n\n"
            "QUAN TRONG: Chi viet van ban thuan tuy (plain text). "
            "KHONG su dung bat ky dinh dang Markdown nao (vi du: khong dung ** , ## , * , - ).\n\n"
            "Chu de: {topic}\n"
            "Thong tin nghien cuu ban dau:\n{research}\n\n"
            "Nhan xet (Critique) can sua:\n{critique}"
        )

    writer_chain = prompt_template | llm | StrOutputParser()
    draft = writer_chain.invoke({
        "topic": topic,
        "research": research,
        "critique": critique
    })
    return {"draft": draft}

# ----- NODE 3: AGENT CRITIC -----
def critic_node(state):
    """
    Agent nay nhan ban nhap (draft) tu state va dua ra nhan xet (critique).
    Quan trong: No phai quyet dinh 'DAT' hoac 'CHUA DAT'.
    """
    print("--- Node: Critic (Dang phe binh) ---")
    draft = state['draft']
    prompt_template = ChatPromptTemplate.from_template(
        "Ban la mot nha phe binh blog kho tinh. Hay doc ban nhap sau va dua ra nhan xet.\n"
        "Neu ban nhap da tot, logic, va du thong tin, hay noi 'DAT'.\n"
        "Neu ban nhap can cai thien (vi du: thieu thong tin, viet te, lac de), "
        "hay chi ra cac diem yeu va noi 'CHUA DAT'.\n\n"
        "Ban nhap:\n{draft}"
    )
    
    critic_chain = prompt_template | llm | StrOutputParser()
    critique = critic_chain.invoke({"draft": draft})
    print(f"Nhan xet: {critique}")
    return {"critique": critique}