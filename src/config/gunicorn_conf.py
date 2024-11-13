
class GunicornConfig:
    # Bind địa chỉ và cổng
    bind = "0.0.0.0:8000"  # Địa chỉ và cổng để Gunicorn lắng nghe

    # Số lượng worker
    # Sử dụng công thức phổ biến: số lượng CPU * 2 + 1

    # workers = multiprocessing.cpu_count() * 2 + 1  # Hoặc đặt số lượng cố định, ví dụ: 6
    workers = 8
    # Kiểu worker
    # Sử dụng `uvicorn.workers.UvicornWorker` để tích hợp Uvicorn làm worker cho FastAPI
    worker_class = "uvicorn.workers.UvicornWorker"

    # Kích thước bộ đệm cho mỗi worker
    worker_connections = 1000  # Kết nối đồng thời tối đa cho mỗi worker (phù hợp cho WebSocket)

    # Thời gian chờ
    timeout = 30  # Thời gian chờ tối đa cho mỗi request (giây)
    keepalive = 5  # Thời gian giữ kết nối mở cho một client (giây)

    # Độ ưu tiên của worker
    # Tùy chọn độ ưu tiên của worker từ 1 đến 20, trong đó mức cao hơn có ưu tiên cao hơn.
    # Gunicorn sẽ cố gắng ưu tiên các workers này khi có yêu cầu xử lý nhiều request.
    worker_priority = 1

    # Thiết lập nhật ký (log)
    accesslog = "-"  # Log truy cập, `-` để ghi vào stdout
    errorlog = "-"   # Log lỗi, `-` để ghi vào stdout
    loglevel = "info"  # Mức độ log: debug, info, warning, error, critical

    # Thời gian chờ khởi tạo worker (trong giây)
    graceful_timeout = 30  # Thời gian cho worker dừng lại trước khi khởi tạo worker mới

    # Thiết lập các cờ (flags) bổ sung
    preload_app = True  # Load toàn bộ ứng dụng trước khi workers chạy, giúp tiết kiệm tài nguyên khi workers khởi tạo lại
    daemon = False  # Nếu True, chạy ứng dụng ở chế độ nền; không nên sử dụng trong phát triển

    # Giới hạn bộ nhớ
    max_requests = 1000  # Số request tối đa cho mỗi worker trước khi khởi tạo lại (giúp giải phóng bộ nhớ)
    max_requests_jitter = 50  # Thêm ngẫu nhiên vào `max_requests` để tránh khởi tạo lại đồng thời các workers

    # Các biến môi trường (Environment Variables) bổ sung
    # raw_env = [
    #     "APP_ENV=production",
    #     "SECRET_KEY=your_secret_key_here"  # Đặt các biến môi trường tùy ý
    # ]

    # Sử dụng SSL nếu cần
    # keyfile = "/path/to/ssl.key"
    # certfile = "/path/to/ssl.crt"

# Tạo một biến cấu hình để Gunicorn nhận diện
gunicornConf = GunicornConfig()
