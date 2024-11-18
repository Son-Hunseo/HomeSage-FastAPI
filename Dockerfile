FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip==24.3.1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV WORKERS=16
ENV THREADS=8

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --workers $WORKERS --workers-per_core $THREADS