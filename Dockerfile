FROM nvcr.io/nvidia/pytorch:22.03-py3
LABEL maintainer="Steven Risch <steve@deepgram.com>"
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update -y && \
    apt-get install -y  ffmpeg python3-pip
RUN pip install flask flask-cors gunicorn

WORKDIR /app

COPY . /app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "300", "app:app"]
