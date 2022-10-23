import pandas as pd

from training_helpers import fit_model, transform_data_for_training, preprocess_data, save_model, evaluate_model


def train_model(data: pd.DataFrame):
    mdf = preprocess_data(data)
    x_test, x_train, y_test, y_train = transform_data_for_training(mdf)
    model = fit_model(x_train, y_train)
    rf_score_test = evaluate_model(model, x_test, x_train, y_test, y_train)

    save_model(model)

    return model, rf_score_test


if __name__ == '__main__':
    data = pd.read_csv("./data/train.csv", encoding="utf-8", sep=",", low_memory=False)
    model, _ = train_model(data)
