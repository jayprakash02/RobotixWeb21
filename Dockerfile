FROM python:3.8-alpine

RUN apk add --no-cache --update --virtual .tmp gcc libc-dev linux-headers make
#cryptography & pillow Postgress
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo py3-setuptools rust postgresql-dev musl-dev
#pillow Prerequisites 
RUN apk add --no-cache tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev 

RUN mkdir /RobotixWeb21
WORKDIR /RobotixWeb21
COPY requirements.txt /RobotixWeb21/
EXPOSE 8000

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk del .tmp \
        libressl-dev \
        musl-dev \
        libffi-dev

COPY . /RobotixWeb21/