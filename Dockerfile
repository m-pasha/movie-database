FROM python:3
WORKDIR /usr/src/docker/Movie-Database
ADD . /usr/src/docker/Movie-Database
RUN pip install -r requirements.txt
