FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip==24.3.1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV WORKERS=4

# 0.0.0.0 으로 해야 외부 네트워크 연결 됨
CMD uvicorn main:app --host 0.0.0.0 --port 8081 --workers $WORKERS