FROM alpine

COPY . /app

RUN apk add socat bash php

WORKDIR /app/Bash-HTTP-Server

CMD [ "./server.sh", "9000" ]
