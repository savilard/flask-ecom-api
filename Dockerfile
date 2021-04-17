FROM python:3.8.6-slim-buster

ENV BUILD_ONLY_PACKAGES='wget' \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.5 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin"

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    python3-pip \
    curl \
    gettext \
    git \
    libpq-dev \
     $BUILD_ONLY_PACKAGES \
    && curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
    && poetry --version \
    && apt-get remove -y $BUILD_ONLY_PACKAGES \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /code

RUN groupadd -r web && useradd -d /code -r -g web web \
    && chown web:web -R /code

COPY --chown=web:web ./pyproject.toml .

RUN mkdir flask_ecom_api \
    && cd flask_ecom_api \
    && touch __init__.py \
    && poetry install

COPY --chown=web:web . .

USER web
