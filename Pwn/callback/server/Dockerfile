FROM python:3-alpine

RUN apk add --no-cache socat

EXPOSE 5000
WORKDIR /challs
COPY files /challs/

# Securing files
RUN chown -R root:root /challs/

# Securing environ
RUN chmod 700 /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/sh /usr/bin/nc /bin/cat /usr/bin/wget /usr/bin/groups /usr/bin/id /bin/ls /usr/bin/vi

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./chall,su=nobody
