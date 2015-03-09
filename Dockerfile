FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /passportfridays
WORKDIR /passportfridays
ADD requirements.txt /passportfridays/
RUN pip install -r requirements.txt
ADD . /code/



