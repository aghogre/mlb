FROM alpine:3.9

RUN  apk add --no-cache --update bash
RUN apk --update add python py-pip gcc openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip 
     
ADD . /MLB

WORKDIR /MLB

RUN  apk add install libfreetype6 
RUN apk add libfreetype6-dev 
RUN apk add install libfontconfig1 
RUN apk add libfontconfig1-dev
RUN  export PHANTOM_JS="phantomjs-2.1.1-linux-i686" && wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \
            && tar xvjf $PHANTOM_JS.tar.bz2 \
            && mv $PHANTOM_JS /usr/local/share \
            && ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

RUN pip install -r requirements.txt

CMD ["/bin/bash", "-c","source arguments.env && python Main.py"]
