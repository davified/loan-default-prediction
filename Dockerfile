FROM python:3.10.6-slim AS prod

WORKDIR /code

RUN apt-get update && apt-get -y install gcc

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml /code/pyproject.toml
RUN poetry install --without dev && rm -rf ~/.cache/pypoetry/{cache,artifacts}

COPY . /code
CMD ["./scripts/start-api-prod.sh"]

FROM prod AS dev

RUN poetry install

CMD ["bash"]
