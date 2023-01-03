import pandas as pd

from training.train import train_model


def test_training_smoke_test():
    data = pd.read_csv("/code/data/train.csv", encoding="utf-8")
    test_data = data.head(10)

    model, score = train_model(test_data)

    assert score >= 0
