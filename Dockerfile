FROM python:3.10.6-slim AS dev

WORKDIR /code

RUN apt-get update && apt-get -y install gcc

RUN pip install poetry
ADD pyproject.toml /code/
RUN poetry config installer.max-workers 10

ENV VENV_PATH="/code/.venv" \
    POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$VENV_PATH/bin:$PATH"

CMD ["bash"]

FROM python:3.10.6-slim AS prod

# FIXME: get multi-stage build to work when poetry install is decoupled from docker build into ./batect setup

WORKDIR /code

ADD requirements.txt src scripts /code/
RUN pip install --no-cache-dir -r /code/requirements.txt

CMD ["/code/scripts/start-api-prod.sh"]
