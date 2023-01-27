#!/bin/sh

set -e

echo "Installing Python 3 if it's not installed..."
which python3 || brew install python3

echo "Installing Poetry if it's not installed..."
which poetry || pip install poetry

echo "Configure poetry to create virtual environment outside of project folder, in default poetry virtualenvs location."
echo "This prevents us from conflating the venv on the host with the venv in the docker container (at /code/.venv)."
poetry config virtualenvs.in-project false

echo "Installing dependencies..."
poetry install

echo "Done. Configure your IDE to use the following virtual environment path: $(poetry env info -p)"