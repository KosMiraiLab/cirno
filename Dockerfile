FROM python:3.11 AS base

WORKDIR /app

RUN apt-get update && \
    apt-get install ffmpeg libavcodec-extra libavfilter-extra -y &&\
    apt-get autoclean &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install poetry &&\
    poetry config virtualenvs.in-project true

FROM base AS builder

COPY poetry.lock pyproject.toml /app/

RUN poetry install


FROM base AS dev

VOLUME ["/app"]

FROM base AS prod

COPY --from=builder /app/ /app/

COPY ./ /app/

RUN chmod +x /app/entrypoint.sh


ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD python bot.py
