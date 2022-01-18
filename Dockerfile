FROM python:3.8
ENV PORT=8000
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn api:app --port $PORT --host 0.0.0.0