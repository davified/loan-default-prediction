import pandas as pd

from training_helpers import fit_model, transform_data_for_training, preprocess_data


def train_model(data: pd.DataFrame):
    mdf = preprocess_data(data)
    x_test, x_train, y_test, y_train = transform_data_for_training(mdf)
    rf_score_t = fit_model(x_test, x_train, y_test, y_train)

    return rf_score_t


if __name__ == '__main__':
    data = pd.read_csv("./data/train.csv", encoding="utf-8", sep=",", low_memory=False)
    train_model(data)
