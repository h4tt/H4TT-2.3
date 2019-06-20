FROM alpine

COPY ./flag1.txt /
COPY ./flag2.txt /app/
COPY ./flag{r34ding_betw33n_th3_1in3s} /app/


RUN apk add shadow; \
    chown 0:0 /app/flag2.txt; \
    chmod 700 /app/flag2.txt; \
    rm -rf /app/flag{r34ding_betw33n_th3_1in3s}

RUN groupadd -g 1337 oof && \
    useradd -r -u 1337 -g oof oof

USER oof