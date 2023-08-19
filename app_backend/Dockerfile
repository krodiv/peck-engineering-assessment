FROM python:3.10-slim as builder

# pin version of poetry
RUN pip install poetry==1.3.1

# poetry configuration for build
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /backend-app

# set dependencies from pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./
RUN touch README.md

# poetry config for not using virtualenv inside docker container
RUN poetry config virtualenvs.create false
# ensure no dev tools are installed in container
RUN poetry install --no-dev

COPY app_backend ./app_backend

CMD source /backend-app/.venv/bin/activate
ENTRYPOINT ["poetry", "run", "python", "-m", "app_backend.app"]