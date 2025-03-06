FROM python:alpine

RUN sed -i 's#https\?://dl-cdn.alpinelinux.org/alpine#https://mirrors.tuna.tsinghua.edu.cn/alpine#g' /etc/apk/repositories && \
    apk add --no-cache socat && adduser -D -h /home/ctf ctf

COPY --chown=ctf:ctf src/chall.py /home/ctf/chall.py
COPY --chown=ctf:ctf --chmod=500 scripts/init.sh /init.sh
COPY --chown=ctf:ctf --chmod=500 scripts/run.sh /run.sh

USER ctf
WORKDIR /home/ctf

CMD [ "/init.sh" ]