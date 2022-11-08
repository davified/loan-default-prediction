FROM python:3.10.6-slim AS prod

WORKDIR /code

RUN apt-get update && apt-get -y install gcc

# how can we avoid copying src directory over before poetry install? this adds a few minutes to our testing cycle
ADD pyproject.toml src /code/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --without dev --no-root && rm -rf ~/.cache/pypoetry/{cache,artifacts}

COPY . /code
CMD ["./scripts/start-api-prod.sh"]

FROM prod AS dev

RUN poetry install

CMD ["bash"]
