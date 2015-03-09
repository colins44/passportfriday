FROM python:2.7
FROM phusion/baseimage
MAINTAINER acmk01 <acmk01@gmail.com>
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install -yq python
RUN apt-get install -yq python-pip
RUN apt-get install -yq python-dev
RUN apt-get install -yq libxml2-dev
RUN apt-get install -yq libpq-dev
RUN apt-get install -yq libmemcached-dev
RUN apt-get install -yq git
RUN apt-get install -yq memcached


RUN mkdir /passportfridays
WORKDIR /passportfridays
ADD requirements.txt /passportfridays/
RUN pip install -r requirements.txt
ADD . /code/

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser


