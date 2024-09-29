FROM python:3.10-alpine 

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && apk update \
    && apk add curl 

COPY . .
EXPOSE 5000

RUN adduser -D devops
USER devops


CMD ["gunicorn", "--bind", "0.0.0.0:5000", "config.wsgi:application"]
