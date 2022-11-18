FROM nvcr.io/nvidia/pytorch:22.03-py3
FROM nvidia/cuda:11.6.0-base-ubuntu20.04
LABEL maintainer="Steven Risch <steve@deepgram.com>"
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update -y && \
    apt-get install -y  ffmpeg python3-pip
RUN pip install gunicorn

WORKDIR /app

COPY . /app

RUN pip3 install -r /app/requirements.txt 

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "300", "app:app"]
