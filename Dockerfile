FROM python:3.9.9
ENV PYTHONBUFFERED 1
RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app