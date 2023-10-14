FROM python:3.11 AS builder

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry && poetry config virtualenvs.in-project true && poetry install

FROM python:3.11 AS worker

WORKDIR /app

COPY --from=builder /app/ /app/ 

COPY ./ /app/

RUN apt-get update && apt-get install ffmpeg -y

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD python bot.py
