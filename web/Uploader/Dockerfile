FROM python:3.10.6

ARG PASSWORD

RUN echo root:${PASSWORD} | chpasswd
RUN apt-get update && apt-get install -y openssh-server curl
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

RUN pip install --upgrade mongoengine uvicorn passlib pycryptodome pytz urllib3 requests
RUN pip install blacksheep==1.2.20

WORKDIR /app

COPY ./src .

COPY ./start.sh .
RUN chmod +x /app/start.sh

CMD ./start.sh