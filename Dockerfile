FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && apk update \
    && apk add curl 

COPY . .
EXPOSE 5000


CMD ["python3", "manage.py", "runserver"]
