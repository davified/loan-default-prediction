import pandas as pd
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split

from training.training_helpers import load_model


class TestMetrics:
    precision_threshold = 0.85

    @classmethod
    def setup_class(cls):
        pass

    def test_global_precision_score_should_be_above_specified_threshold(self):
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
        precision = precision_score(y_test, y_pred, average="weighted")

        # assert on metric
        assert precision >= self.precision_threshold

    def test_stratified_precision_score_should_be_above_specified_threshold(self):
        pipeline = load_model()

        data = pd.read_csv("./data/train.csv", encoding="utf-8", low_memory=False)
        strata_col_name = "GENDER"
        stratas = data["GENDER"].unique().tolist()
        y = data["DEFAULT"]
        X = data.drop("DEFAULT", axis=1)
        X_test, X_train, y_test, y_train = train_test_split(X, y, random_state=10)

        # get predictions and metric for each strata
        precision_scores = []
        for strata in stratas:
            X_test_stratified = X_test[X_test[strata_col_name] == strata]
            y_test_stratified = y_test[y_test.index.isin(X_test_stratified.index)]
            y_pred_stratified = pipeline.predict(X_test_stratified)

            # calculate metric
            precision_for_single_strata = precision_score(y_test_stratified, y_pred_stratified, average="weighted")
            print(f"{strata}: precision score: {precision_for_single_strata}")

            precision_scores.append(precision_for_single_strata)

        assert all(precision > self.precision_threshold for precision in precision_scores)
