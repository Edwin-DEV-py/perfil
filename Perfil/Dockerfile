FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
    
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    python3-dev

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app