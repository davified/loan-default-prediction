#!/bin/sh

set -e

echo "Installing homebrew if it's not installed..."
which brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# Prevent homebrew from running brew update --auto-update when running brew install, which can take quite long if user has many outdated packages
export HOMEBREW_NO_AUTO_UPDATE=1

echo "Installing pyenv if it's not installed"
if command -v pyenv &> /dev/null; then
  PYENV_VERSION_INSTALLED=$(pyenv --version | awk '{print $2}')
  echo "pyenv is already installed (version: $PYENV_VERSION_INSTALLED). Skipping installation"
else
  export PYENV_GIT_TAG="v2.4.0"
  echo "Installing pyenv $PYENV_GIT_TAG"
  curl https://pyenv.run | bash
fi

echo "Configuring pyenv"
./scripts/configure-pyenv.sh
source ~/.bashrc

PYTHON_VERSION="3.10.12"
echo "Installing Python $PYTHON_VERSION and setting to use locally"
pyenv install "$PYTHON_VERSION" --skip-existing
pyenv local "$PYTHON_VERSION"

echo "Using python $(python3 --version)"

echo "Installing docker if it's not installed..."
which docker || brew install --cask docker

echo "Installing java (needed by batect) if it's not installed..."
which java || brew install --cask adoptopenjdk

echo "Installing dependencies on host (so that we can configure a virtual environment for our IDE)"
./scripts/go/install-dependencies-on-host.sh
