FROM ubuntu:22.04 AS base

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN apt-get upgrade -y
RUN pip3 install -U pip

RUN pip3 install poetry


# develop
FROM base AS develop

WORKDIR /usr/local/libs

COPY src/pyproject.toml ./
COPY src/poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

WORKDIR /opt/dev


# release
FROM base AS release

WORKDIR /usr/local/libs

COPY src/pyproject.toml ./
COPY src/poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

WORKDIR /opt

ENV WORKSPACE=/opt

EXPOSE 8000

COPY src/app /opt/app
COPY src/config /opt/config

CMD ["gunicorn", "app.main:app", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "--timeout", "30", "-b", "0.0.0.0:8000", "--limit-request-line", "0", "--limit-request-field_size", "0", "--log-level", "debug"]
