#!/bin/sh

set -e

python -m unittest discover tests/model_training
