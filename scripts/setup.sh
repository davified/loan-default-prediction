#!/bin/sh

set -e

echo "Installing dependencies in virtual environment: $VENV_PATH"
python3 -m venv $VENV_PATH
. $VENV_PATH/bin/activate
poetry install
