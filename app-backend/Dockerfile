FROM python:3.10-slim as builder

RUN pip install poetry==1.3.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /backend-app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

#RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR
#
# FROM python:3.10-slim as runtime
#
# FROM python:3.11-slim-buster as runtime
#
# ENV VIRTUAL_ENV=/app/.venv \
#     PATH="/app/.venv/bin:$PATH"
# COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY app_backend ./app_backend

CMD source /backend-app/.venv/bin/activate
# EXPOSE 5000/tcp
ENTRYPOINT ["poetry", "run", "python", "-m", "app_backend.app"]