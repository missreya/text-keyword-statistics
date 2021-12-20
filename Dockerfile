FROM python:3.9
WORKDIR /usr/src/app
COPY ./text_keyword_statistics.py /usr/src/app
RUN pip install numpy