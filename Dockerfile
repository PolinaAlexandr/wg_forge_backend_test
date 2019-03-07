FROM python:3.6-alpine as builder

WORKDIR cat_service

COPY requirements.txt .

RUN apk add build-base python3-dev postgresql-dev musl-dev linux-headers nginx && \
    pip install -r requirements.txt

FROM builder

WORKDIR cat_service

COPY . .

RUN mkdir -p /etc/nginx/sites-available/ && mkdir -p /etc/nginx/sites-enabled/ && \
    cp cat_service_nginx.conf /etc/nginx/sites-available && \
    ln -s  /etc/nginx/sites-available/cat_service.conf /etc/nginx/sites-enabled/

EXPOSE 8080

CMD sh start_service --release
