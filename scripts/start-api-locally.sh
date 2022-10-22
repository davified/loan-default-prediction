#!/bin/bash

set -e

uvicorn src.api.app:app --reload
