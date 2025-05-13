FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install gcc libpq-dev curl -y \
    && apt-get clean

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/
