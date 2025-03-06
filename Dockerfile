FROM python:3.11-slim-buster

WORKDIR /django-code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat gcc build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /django-code/

RUN pip install -r requirements.txt

COPY . /django-code/

