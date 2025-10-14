FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY artifacts/ ./artifacts/
COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:${PORT}", "application:application"]