# Dockerfile

# Stage 1: Build dependencies
FROM python:3.9-slim AS builder

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file yêu cầu để cài đặt các thư viện
COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH
COPY src/ /app/src/
COPY requirements.txt /app/
COPY .env /app/
ENV PYTHONPATH="${PYTHONPATH}:/app/src"



CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "--log-level", "debug", "src.main:app"]
# CMD ["python", "src/main.py"]
