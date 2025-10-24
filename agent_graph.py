from typing import TypedDict
from langgraph.graph import StateGraph, END

# Import cac node tu file agent_nodes.py
from agent_nodes import researcher_node, writer_node, critic_node

# 1. Dinh nghia "Ban lam viec" (State)
class AgentState(TypedDict):
    topic: str
    research: str
    draft: str
    critique: str

# 2. Dinh nghia Ham Logic (Dieu huong)
def should_continue(state: AgentState):
    """
    Ham quyet dinh luong di tiep theo sau khi Critic lam viec.
    """
    print("--- Node: Logic (Quyet dinh) ---")
    critique = state['critique']

    if "CHUA DAT" in critique.upper():
        print("--- Phe binh: CHUA DAT. Yeu cau viet lai! ---")
        return "writer"
    else:
        print("--- Phe binh: DAT. Hoan thanh! ---")
        return END

# 3. Rap "Hoi dong" (Graph)
def compile_graph():
    """
    Tao va bien dich graph.
    """
    workflow = StateGraph(AgentState)

    # Them cac node
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("critic", critic_node)

    # Dat diem bat dau
    workflow.set_entry_point("researcher")

    # Ve cac duong noi
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "critic")

    # Them duong noi co dieu kien
    workflow.add_conditional_edges(
        "critic",
        should_continue,
        {
            "writer": "writer",
            END: END
        }
    )

    # Bien dich graph
    app = workflow.compile()
    print("--- 'Hoi dong' (Graph) da duoc bien dich thanh cong! ---")
    return app

# Tao bien 'app' de file main.py co the import
app = compile_graph()