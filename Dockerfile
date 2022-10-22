FROM python:3.9.14-slim

RUN apt-get update

WORKDIR /code

COPY requirements.txt /code/requirements.txt
COPY requirements-dev.txt /code/requirements-dev.txt
RUN pip install -r requirements-dev.txt

# Configure PYTHONPATH so that packages/modules in src are symmetrically available to tests
# (doesn't include other clients - e.g. IDE, which require this to be set in their own config - e.g. .vscode/settings.json or .idea/xxx.iml)
ENV PYTHONPATH=/code/src

CMD ["bash"]