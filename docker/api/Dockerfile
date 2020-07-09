FROM python:3.8-slim-buster

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
VOLUME /usr/src/app
WORKDIR /usr/src/app
CMD python manage.py runserver 0.0.0.0:8000