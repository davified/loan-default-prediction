# Credit Score Prediction

An end-to-end example of how to apply software engineering practices for ML training, testing and deployment.

tasks:
- ✅ make src/ directory work (for tests, main script and IDE )
- ✅ use Poetry instead of pip: https://nanthony007.medium.com/stop-using-pip-use-poetry-instead-db7164f4fc72
- ✅ setup Dockerfile (for training locally)
- ✅ remove poetry.lock and install via docker build again - see if poetry.lock file is created - it's in the image, but runtime volume mount overrides it
- ✅ setup Dockerfile (for API development)
- ✅ setup github actions (for training on cloud)
- ✅ add batect
- ✅ research: how people ensure cross-platform (M1 and non-M1 macs) compatibility when working with Docker
- remove ENV PYTHONPATH=/code/src, and make sure everything works (IDE, CLI)
- ✅ setup Dockerfile (for API deployment)
- ✅ Refactor Dockerfile (into multi-stage build)
- make prod image smaller
- optimize Dockerfile (currently, ADD src runs before poetry install ,and makes everything small)
- configure Docker/batect cache to speed up 
- use pytest instead of unittest: https://docs.pytest.org/en/7.1.x/how-to/output.html
- enhancements:
  - poetry.lock file is trapped in docker build. other poetry docker best practices: https://github.com/python-poetry/poetry/discussions/1879
  - add batect caches on CI (https://batect.dev/docs/using-batect-with/ci/github-actions/#caching-between-builds)

## Setup

```shell script
# mac users
scripts/go-mac.sh

# linux users
scripts/go-linux-ubuntu.sh

# windows
# work in progress. in the meantime, please install Docker manually if it's not already installed
```

Configure Docker runtime
```shell
# set up colima (a license-free docker runtime, an alternative to docker desktop)
https://gist.github.com/jcartledge/0ce114e9719a62a4776569e80088511d
```

Configure your IDE to use the python virtual environment (`./.venv/`) created by `go.sh` 
- [PyCharm instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment)
- [VS Code instructions](https://code.visualstudio.com/docs/python/environments)

## Tasks that you can run

```shell script
# start docker runtime
colima start

# build image
docker build -t credit-score-prediction:dev .

# start container (i.e. local dev environment)
docker run -it --rm -v $(pwd):/code -p 80:80 credit-score-prediction:dev bash

### in the dev container

# run model training smoke tests
scripts/tests/smoke-test-model-training.sh

# train model
scripts/train-model.sh 

# run api tests
scripts/tests/api-test.sh

# start API in development mode
scripts/start-api-locally.sh

# send requests to API locally (run this from another terminal outside of the Docker container, as it uses curl, which we haven't installed)
scripts/curl-local-api.sh

# start jupyter notebook
jupyter notebook --ip 0.0.0.0 --allow-root
```

## Sources and attributions

- original notebook and data: https://www.kaggle.com/code/mohamedsalemmohamed/credit-score-10-classification-algorithms-eda