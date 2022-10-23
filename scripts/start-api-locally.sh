#!/bin/bash

set -e

uvicorn src.api.app:app --host 0.0.0.0 --port 80 --reload
# docs: https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi
