FROM python:3.10
RUN apt-get update && apt-get install -y libzbar0 ffmpeg libsm6 libxext6  -y
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt /opt/qr_detect_app/requirements.txt
RUN cd /opt/qr_detect_app/ && pip install -r requirements.txt
COPY qr_detect.py /opt/qr_detect_app/
COPY qr_codes/ /opt/qr_detect_app/qr_codes/
WORKDIR /opt/qr_detect_app/
RUN python qr_detect.py
