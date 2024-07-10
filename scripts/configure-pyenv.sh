#!/bin/bash

set -e

pyenv_config_line_0='# pyenv'
pyenv_config_line_1='export PYENV_ROOT="$HOME/.pyenv"'
pyenv_config_line_2='command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"'
pyenv_config_line_3='eval "$(pyenv init -)"'

add_pyenv_config_if_not_exists() {
  local file="$1"
  if ! grep -Fxq "$pyenv_config_line_1" "$file"; then
    echo "$pyenv_config_line_0" >> "$file"
    echo "$pyenv_config_line_1" >> "$file"
    echo "$pyenv_config_line_2" >> "$file"
    echo "$pyenv_config_line_3" >> "$file"
    echo "Added pyenv config to $file"
  else
    echo "Already exists: $line"
  fi
}

# Add config to both ~/.bashrc and ~/.zshrc
for file in "$HOME/.bashrc" "$HOME/.zshrc"; do
  add_pyenv_config_if_not_exists "$file"
done

