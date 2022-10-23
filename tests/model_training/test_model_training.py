import unittest

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from train import train_model


class TestModelTraining(unittest.TestCase):
    def test_train_model_trains_a_model_with_metric_above_specified_threshold(self):
        data = pd.read_csv("./data/train.csv", encoding="utf-8", sep=",", low_memory=False)
        test_data = data.head(10)
        model, score = train_model(test_data)

        self.assertIsInstance(model, RandomForestClassifier)
        self.assertGreaterEqual(score, 0.5)
