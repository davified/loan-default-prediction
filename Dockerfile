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
