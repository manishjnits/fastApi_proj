FROM python:3.10-slim

WORKDIR /code

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

EXPOSE 8000
