#!/bin/sh

set -e

echo "Installing Python 3 if it's not installed..."
which python3 || brew install python3

echo "Installing Poetry if it's not installed..."
which poetry || pip install poetry

echo "Configure poetry to create virtual environment outside of project folder, in default poetry virtualenvs location."
echo "This avoids confusing us/Poetry with an in-project virtual environment either in the container or on host"
poetry config virtualenvs.in-project false

echo "Installing dependencies on host..."
poetry install

echo "Done. Configure your IDE to use the following virtual environment path: $(poetry env info -p)"