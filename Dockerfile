FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --virtual .tmp gcc libc-dev linux-headers libressl-dev musl-dev libffi-dev cargo
# Add --no-cache in Production above command
RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt
# RUN apk del .tmp \
        # libressl-dev \
        # musl-dev \
        # libffi-dev

RUN mkdir /RobotixWeb21
COPY ./RobotixWeb /RobotixWeb21
COPY ./apps /RobotixWeb21
COPY ./manage.py /RobotixWeb21

WORKDIR /RobotixWeb21

COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD [ "entrypoint.sh" ]
