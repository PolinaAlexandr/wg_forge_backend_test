FROM python:3.6-alpine as builder

WORKDIR cat_service

COPY requirements.txt .

RUN apk add build-base python3-dev postgresql-dev musl-dev linux-headers && \
    pip install -r requirements.txt

FROM builder

WORKDIR cat_service

COPY . .

EXPOSE 8080

#CMD uwsgi --http :8080 --wsgi-file cat_service/wsgi.py --master --processes 4 --threads 2
CMD sh start_service --release
