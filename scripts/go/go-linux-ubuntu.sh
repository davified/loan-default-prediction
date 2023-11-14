#!/bin/sh

set -e

echo "Updating apt package index"
sudo apt-get update

echo "Installing python3 if it's not installed..."
which python3 || sudo apt install -y python3

echo "Installing docker if it's not installed..."
which docker || sudo apt install docker.io

echo "Verifying if docker has installed successfully..."
docker --version

echo "Installing java (needed by batect) if it's not installed..."
which java || sudo apt install default-jdk

echo "Installing pip if it's not installed..."
which pip || sudo apt install -y python3-pip

echo "Installing dependencies on host..."
./scripts/go/install-dependencies-on-host.sh