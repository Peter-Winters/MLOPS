FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt install awscli -y
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
