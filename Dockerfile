FROM python:3.6-alpine

WORKDIR cat_service

COPY . .

RUN apk add build-base python3-dev postgresql-dev musl-dev linux-headers && \
    pip install -r requirements.txt

EXPOSE 8080

#CMD uwsgi --http :8080 --wsgi-file cat_service/wsgi.py --master --processes 4 --threads 2
CMD ./start_service --release
