#!/bin/sh

set -e

poetry install --no-root

# for prod stage in Dockerfile
poetry export -f requirements.txt >> requirements.txt
