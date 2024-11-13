FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH
COPY src/ /app/src/
COPY requirements.txt /app/
COPY health_check.sh /app/health_check.sh
RUN apt-get update && apt-get install -y curl
ENV PYTHONPATH="${PYTHONPATH}:/app/src"



CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "--log-level", "debug", "src.main:app"]
# CMD ["python", "src/main.py"]
