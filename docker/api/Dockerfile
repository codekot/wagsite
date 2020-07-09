FROM python:3.8-slim-buster

RUN apt-get update -qq && apt-get install -y \
  build-essential libsqlite3-dev libpng-dev libjpeg-dev

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
VOLUME /usr/src/app
WORKDIR /usr/src/app
CMD python manage.py runserver 0.0.0.0:8000