#################### first stage: dev ####################
FROM python:3.10-slim-bookworm AS dev

WORKDIR /code

RUN apt-get update && apt-get -y install gcc g++

RUN pip install --upgrade pip && \
        pip install poetry
ADD pyproject.toml /code/
RUN poetry config installer.max-workers 10
RUN poetry config virtualenvs.create false

ARG VENV_PATH
ENV VENV_PATH=$VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

CMD ["bash"]

#################### second stage: builder ####################
FROM dev AS builder

COPY poetry.lock /code
RUN poetry export --without dev --format requirements.txt --output requirements.txt

#################### third stage: prod ####################
FROM python:3.10-slim-bookworm AS prod

WORKDIR /code
COPY src /code/src
COPY scripts /code/scripts
COPY artifacts /code/artifacts
COPY --from=builder /code/requirements.txt /code
RUN pip install --no-cache-dir -r /code/requirements.txt
CMD ["./scripts/start-api-prod.sh"]
