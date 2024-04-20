FROM ubuntu:22.04
RUN apt-get update && \
    apt-get -y install python3 socat python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pycryptodome ecdsa

WORKDIR /home/nobody
COPY src .

ENV FLAG=LKS{EcD5A_iS_4bSoLut3Ly_S1mPl3}

USER nobody
EXPOSE 10000
CMD socat TCP-LISTEN:10000,reuseaddr,fork EXEC:"python3 -u chall.py"
