#!/bin/sh

set -e

echo "Updating apt package index"
sudo apt-get update

echo "Installing python3 if it's not installed..."
which python3 || sudo apt install -y python3

echo "Installing pip if it's not installed..."
which pip || sudo apt install -y python3-pip

echo "Installing lefthook if it's not installed..."
which lefthook || curl -1sLf 'https://dl.cloudsmith.io/public/evilmartians/lefthook/setup.deb.sh' | sudo -E bash
which lefthook || sudo apt install lefthook

echo "Setting up git hooks for this project"
lefthook install

echo "Installing dependencies on host..."
./scripts/go/install-dependencies-on-host.sh