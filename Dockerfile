FROM python:3.9-slim
WORKDIR /code
RUN apt update && apt install awscli -y
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
EXPOSE 5000
CMD ["flask", "run"]