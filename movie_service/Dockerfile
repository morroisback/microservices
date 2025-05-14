FROM python:3.13.3-slim AS builder

WORKDIR /workspace/

RUN apt-get update \
    && apt-get install gcc libpq-dev -y \
    && apt-get clean

COPY ./requirements.txt /workspace/requirements.txt

RUN pip install --no-cache-dir --prefix=/install -r /workspace/requirements.txt 

FROM python:3.13.3-slim

WORKDIR /workspace/

RUN apt-get update \
    && apt-get install libpq5 curl -y \
    && apt-get clean

COPY --from=builder /install /usr/local

COPY . /workspace/