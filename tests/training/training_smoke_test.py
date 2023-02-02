import pandas as pd
from sklearn.pipeline import Pipeline

from training.train import train_model


def test_training_smoke_test():
    data = pd.read_csv("/code/data/train.csv", encoding="utf-8", low_memory=False)

    g = data.groupby('DEFAULT')
    test_sample_size = 10
    test_data = g.apply(lambda df: df.head(test_sample_size).reset_index(drop=True)).reset_index(drop=True)

    pipeline = train_model(test_data)

    assert isinstance(pipeline, Pipeline)
