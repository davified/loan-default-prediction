#!/bin/sh

set -e

echo "Installing homebrew if it's not installed..."
which brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# Prevent homebrew from running brew update --auto-update when running brew install, which can take quite long if user has many outdated packages
export HOMEBREW_NO_AUTO_UPDATE=1

echo "Installed pyenv as we need to target a specific version due to library dependancies"
brew install pyenv

echo "Installing 3.10 and setting to use locally"
pyenv install 3.10.0
pyenv local 3.10.0

echo "Setting Poetry to use this for the Poetry project"
poetry env use 3.10.10

echo "Installing docker if it's not installed..."
which docker || brew install --cask docker

echo "Installing java (needed by batect) if it's not installed..."
which java || brew install --cask adoptopenjdk

echo "Installing dependencies on host (so that we can configure a virtual environment for our IDE)"
./scripts/go/install-dependencies-on-host.sh
