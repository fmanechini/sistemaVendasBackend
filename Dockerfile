FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev 
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /sistemaVendasApp
WORKDIR /sistemaVendasApp
COPY ./sistemaVendasApp /sistemaVendasApp

RUN adduser --disabled-password --gecos '' user
USER user
