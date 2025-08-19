FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y sudo

# Create user and set password
RUN useradd -m -s /bin/bash tehuan && \
    echo "tehuan:1234" | chpasswd && \
    usermod -aG sudo tehuan

RUN chown -R tehuan:tehuan /home/tehuan

USER tehuan
WORKDIR /home/tehuan

ENV PATH="/home/tehuan/.local/bin:$PATH"