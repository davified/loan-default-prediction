import pandas as pd
import pytest
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split

from training.training_helpers import load_model


class TestMetrics:
    recall_threshold = 0.65

    def test_global_recall_score_should_be_above_specified_threshold(self):
        # load trained model
        pipeline = load_model()

        # load test data
        data = pd.read_csv("./data/train.csv", encoding="utf-8", low_memory=False)
        y = data["DEFAULT"]
        X = data.drop("DEFAULT", axis=1)
        X_test, X_train, y_test, y_train = train_test_split(X, y, random_state=10)

        # get predictions
        y_pred = pipeline.predict(X_test)

        # calculate metric
        recall = recall_score(y_test, y_pred, average="weighted")

        # assert on metric
        print(f"global recall score: {recall}")
        assert recall >= self.recall_threshold

    @pytest.mark.skip
    def test_stratified_recall_score_should_be_above_specified_threshold(self):
        pipeline = load_model()

        data = pd.read_csv("./data/train.csv", encoding="utf-8", low_memory=False)
        strata_col_name = "OCCUPATION_TYPE"
        stratas = data["OCCUPATION_TYPE"].unique().tolist()
        y = data["DEFAULT"]
        X = data.drop("DEFAULT", axis=1)
        X_test, X_train, y_test, y_train = train_test_split(X, y, random_state=10)

        # get predictions and metric for each strata
        recall_scores = []
        for strata in stratas:
            X_test_stratified = X_test[X_test[strata_col_name] == strata]
            y_test_stratified = y_test[y_test.index.isin(X_test_stratified.index)]
            y_pred_stratified = pipeline.predict(X_test_stratified)

            # calculate metric
            recall_for_single_strata = recall_score(y_test_stratified, y_pred_stratified, average="weighted")
            print(f"{strata}: recall score: {recall_for_single_strata}")

            recall_scores.append(recall_for_single_strata)

        assert all(recall > self.recall_threshold for recall in recall_scores)
