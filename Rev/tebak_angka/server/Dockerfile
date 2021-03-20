FROM ubuntu:20.04

WORKDIR /challs

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt install socat gcc -y

COPY ./binary /challs

RUN gcc -otebak_angka tebak_angka.c
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls
RUN chown root:root -R /challs

EXPOSE 5000

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./tebak_angka,su=nobody
