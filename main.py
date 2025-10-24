import os
from dotenv import load_dotenv

# Nap bien moi truong (API key) tu file .env
load_dotenv()

# Kiem tra xem API key da duoc nap chua
if not os.environ.get("GOOGLE_API_KEY"):
    print("Loi: Khong tim thay GOOGLE_API_KEY.")
    print("Vui long tao file .env va them API key vao do.")
    exit()

print("--- Da nap API Key thanh cong ---")

# Import 'app' tu file agent_graph.py (sau khi da nap API key)
try:
    from agent_graph import app
except Exception as e:
    print(f"Loi khi import graph: {e}")
    exit()

def run_agent_team():
    # 1. Yeu cau nguoi dung nhap chu de
    user_topic = input("\nVui long nhap chu de ban muon 'Hoi dong' thuc hien: ")

    # 2. Tao dictionary 'inputs' tu chu de do
    inputs = {"topic": user_topic}

    print(f"\n--- Dang giao viec cho 'Hoi dong' voi chu de: \"{inputs['topic']}\" ---")
    print("Vui long cho...")

    # 3. Chay .invoke()
    try:
        final_state = app.invoke(inputs)
        
        print("\n" + "="*50)
        print("--- HOI DONG DA HOAN THANH CONG VIEC ---")
        print("="*50 + "\n")

        # 4. In ket qua cuoi cung
        print("BAI VIET HOAN CHINH (PHIEN BAN DA DUOC DUYET):\n")
        print(final_state['draft'])

    except Exception as e:
        print(f"\nLoi xay ra trong qua trinh chay agent: {e}")

if __name__ == "__main__":
    run_agent_team()