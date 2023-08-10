# Credit Score Prediction

An end-to-end example of how to apply software engineering practices for ML training, testing and deployment.

## Setup

1. Install OS-level dependencies

```shell script
# mac users
scripts/go/go-mac.sh

# linux users
scripts/go/go-linux-ubuntu.sh

# windows
scripts\go\install_choco.ps1
scripts\go\install.bat
```

2. Install and configure Docker runtime

- Option 1: Use **Colima** (a license-free docker runtime, an alternative to docker desktop):
    - Follow steps here: https://gist.github.com/jcartledge/0ce114e9719a62a4776569e80088511d
- Option 2: Use **Docker Desktop**, if you have a Docker Desktop license, or a eligible to use it for free (see [Docker Desktop license agreement](https://docs.docker.com/subscription/desktop-license/))
    - Follow steps here: https://docs.docker.com/desktop/

> ** Note **
For this exercise, we will use Option 1 (colima) to demonstrate how to use docker containers in cases where Docker Desktop licenses aren't available.

> ** Note **
Typically, the commands that you've just run would be part of a team's go script. But, to provide flexibility and accommodate the circumstances of various readers, we've extracted this as a separate manual step.

3. Configure your IDE to use the python virtual environment created by the go scripts
- [PyCharm instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment)
- [VS Code instructions](https://code.visualstudio.com/docs/python/environments)

## Getting started

Build and start local development environment.

```shell
# start docker runtime
colima start

# install dependencies in local dev image
./batect --output=all setup

# start container (i.e. local dev environment)
./batect start-dev-container

```

Here are common tasks that you can run in the dev container during development.

```shell
# run model training smoke tests
scripts/tests/smoke-test-model-training.sh

# train model
scripts/train-model.sh 

# run api tests
scripts/tests/api-test.sh

# exit container
exit # or hit Ctrl + D
```

You can also run these as batect tasks from the host (e.g. `./batect train-model`, `./batect api-test`) 

For the following commands, you have to run it as batect tasks because the port mappings are defined at the level of each task. For example, in `batect.yml`, the `start-jupyter` task exposes port 8888 and makes it accessible from the host.

if you don't need
```sh
# start jupyter notebook
./batect start-jupyter

# start API in development mode
./batect start-api-locally

# send requests to API locally (run this from another terminal outside of the Docker container, as it uses curl, which we haven't installed)
scripts/request-local-api.sh
```

## Sources and attributions

- original data: https://www.kaggle.com/competitions/will-they-default-devday19/data