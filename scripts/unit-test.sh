#!/bin/sh

set -e

echo "Creating virtual environment..."
python -m venv /code/.venv-dev

echo "Activating virtual environment..."
. /code/.venv-dev/bin/activate

echo "Installing python dev dependencies..."
pip install --upgrade pip
pip install -r requirements-dev.txt

python -m unittest discover ./tests/
