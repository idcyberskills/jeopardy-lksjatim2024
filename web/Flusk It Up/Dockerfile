FROM python:3.11-slim-buster

ARG PASSWORD

WORKDIR /opt

RUN apt-get update
RUN apt-get install -y nano openssh-server \
    gcc python-dev python3-dev libgmp3-dev curl

RUN echo root:${PASSWORD} | chpasswd
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

RUN pip install flask

COPY src/ .

ENV FLASK_APP=app
CMD ["python","main.py"]
