FROM python:3.10.6-slim AS dev

WORKDIR /code

RUN apt-get update && apt-get -y install gcc

ADD pyproject.toml poetry.lock src /code/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
RUN poetry export -f requirements.txt >> requirements.txt

CMD ["bash"]

FROM python:3.10.6-slim AS prod

ADD src scripts /code/
COPY --from=dev /code/requirements.txt /code
RUN pip install --no-cache-dir -r /code/requirements.txt

CMD ["./scripts/start-api-prod.sh"]
