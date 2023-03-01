FROM python:3.9-alpine

WORKDIR /app

COPY ./code/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./code/*.py .

EXPOSE 5000