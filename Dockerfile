FROM alpine:3.9

RUN  apk add --no-cache --update bash
RUN apk --update add python py-pip gcc openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip 
     
ADD . /MLB

WORKDIR /MLB

RUN pip install -r requirements.txt

CMD ["/bin/bash", "-c","source arguments.env && python Main.py"]
