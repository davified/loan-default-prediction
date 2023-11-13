#!/bin/sh

set -e

echo "Installing poetry if it's not installed..."
which poetry || curl -sSL https://install.python-poetry.org | python3 -

echo "Configure poetry to create virtual environment outside of project folder, in default poetry virtualenvs location."
poetry config virtualenvs.in-project false

echo "Installing dependencies..."
poetry install

echo "Done. Configure your IDE to use the following virtual environment path: $(poetry env info -p)/bin/python"