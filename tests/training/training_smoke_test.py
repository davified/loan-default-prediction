import unittest

import pandas as pd

from training.train import train_model


class TrainingSmokeTest(unittest.TestCase):
    def test_train_model_runs_to_completion_without_error(self):
        data = pd.read_csv("/code/data/train.csv", encoding="utf-8")
        test_data = data.head(10)

        model, score = train_model(test_data)

        assert score >= 0
