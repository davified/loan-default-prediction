# Credit Score Prediction

An end-to-end example of how to apply software engineering practices for ML training, testing and deployment.

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