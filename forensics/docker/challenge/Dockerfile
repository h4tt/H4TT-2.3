FROM alpine

COPY ./flag{r34ding_betw33n_th3_1in3s} /app/flag
COPY ./flag1.txt /
COPY ./flag2.txt /app

RUN rm -rf /app/flag; \
    chown 0:0 /app/flag2.txt; \
    chmod 700 /app/flag2.txt; \
    apk add shadow;

RUN groupadd -g 1337 oof && \
    useradd -r -u 1337 -g oof oof
USER oof