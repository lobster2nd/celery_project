FROM python:3.11-alpine

WORKDIR /app

COPY ./mysite .
COPY ./requirements.txt .
COPY ./run.sh .

RUN apk add --no-cache libmagic \
    && pip install -r requirements.txt

ENV PYRHONUNBUFFERED=1

CMD ["sh", "run.sh"]