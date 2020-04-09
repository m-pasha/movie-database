FROM alpine:3.11 as build

RUN apk update
RUN apk add --upgrade --no-cache "postgresql-client" "postgresql-contrib" "postgresql-dev" bash curl
RUN apk add --upgrade --no-cache py-pip g++ python-dev linux-headers gcc make libffi-dev uwsgi-python uwsgi wget

RUN apk add --upgrade --no-cache python3 python3-dev

ADD requirements/ /tmp

RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/base.txt


ADD . /api/src/

EXPOSE 8000

WORKDIR /api/src/

FROM build as dev
ENV RQFILE=dev.txt
RUN if [ -f /tmp/$RQFILE ]; then pip3 install -r /tmp/$RQFILE; else pip3 install -r /tmp/base.txt; fi

FROM build as prod
ENV RQFILE=base.txt
RUN if [ -f /tmp/$RQFILE ]; then pip3 install -r /tmp/$RQFILE; else pip3 install -r /tmp/base.txt; fi
