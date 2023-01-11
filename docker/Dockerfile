FROM python:3.8.15-buster as python-base

WORKDIR /home/python-base/project

COPY ./requirements.txt /home/python-base/project

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install git bash libzip-dev unzip

RUN groupadd --gid 1000 python-base \
  && useradd --uid 1000 --gid python-base --shell /bin/bash --create-home python-base \
  && pip install -r requirements.txt