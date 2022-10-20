#!/bin/sh

set -e

# 1. update apt package index
apt-get update

# 2. install Docker from the official repo
apt-get install docker.io

# 3. test if docker has installed successfully
docker --version
