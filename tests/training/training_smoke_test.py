import pandas as pd
from sklearn.pipeline import Pipeline

from training.train import train_model


def test_training_smoke_test():
    data = pd.read_csv("/code/data/train.csv", encoding="utf-8", low_memory=False)
    # group by target column to ensure we train on data that contains all target labels:
    test_data = data.groupby('DEFAULT').apply(lambda df: df.head(10)).reset_index(drop=True)

    pipeline = train_model(test_data)

    predictions = pipeline.predict(test_data)
    valid_predictions = {0, 1}
    assert valid_predictions.issubset(predictions)

