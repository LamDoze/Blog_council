# Dự án "Hội đồng" Agent AI (Agent Team Project)

Đây là một dự án Python đơn giản sử dụng LangGraph để tạo ra một nhóm các agent AI (một "hội đồng") làm việc cùng nhau để hoàn thành một nhiệm vụ: Nghiên cứu và viết một bài blog ngắn.

## Các thành viên "Hội đồng"
1.  Researcher: Tìm kiếm thông tin về chủ đề được giao bằng DuckDuckGo.
2.  Writer: Dựa trên thông tin, viết một bản nháp bài blog.
3.  Critic: Đánh giá bản nháp. Nếu "ĐẠT", quy trình kết thúc. Nếu "CHƯA ĐẠT", `Writer` sẽ phải viết lại dựa trên nhận xét.

## Cài đặt

1.  Clone kho lưu trữ này:
    ```bash
    git clone [https://github.com/TEN_CUA_BAN/TEN_REPO_CUA_BAN.git](https://github.com/TEN_CUA_BAN/TEN_REPO_CUA_BAN.git)
    cd TEN_REPO_CUA_BAN
    ```

2.  Tạo một môi trường ảo (khuyến nghị):
    ```bash
    python -m venv venv
    Windown:
    venv\Scripts\activate
    ```

3.  Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```

## Cấu hình
1.  Dự án này cần một API Key của Google Gemini (Google AI Studio).
2.  Tạo một file tên là `.env` trong thư mục gốc của dự án.
3.  Thêm API key của bạn vào file đó:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
    (File `.gitignore` đã được cấu hình để bỏ qua file này, đảm bảo an toàn cho key của bạn).

## Chạy dự án
Chạy file `main.py` từ terminal:
```bash
python main.py