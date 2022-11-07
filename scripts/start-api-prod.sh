#!/bin/bash

set -e

uvicorn src.api.app:app --host 0.0.0.0 --port 80
