import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder

from training.training_helpers import save_model


def train_model(data: pd.DataFrame):
    categorical_columns = ["CONTRACT_TYPE", "GENDER", "INCOME_TYPE", "FAMILY_STATUS", "HOUSING_TYPE",
                           "ORGANIZATION_TYPE", "NAME_TYPE_SUITE",
                           "WEEKDAY_APPR_PROCESS_START"  # temp workaround
                           ]
    ordinal_columns = ["FLAG_OWN_CAR", "FLAG_OWN_REALTY", "EDUCATION_TYPE"]
    numerical_columns = ["COUNT_CHILDREN", "INCOME", "AMT_CREDIT", "AMT_ANNUITY",
                         "REGION_POPULATION_RELATIVE",
                         "DAYS_BIRTH", "DAYS_EMPLOYED", "DAYS_REGISTRATION", "DAYS_ID_PUBLISH", "REGION_RATING_CLIENT",
                         "HOUR_APPR_PROCESS_START", "REG_REGION_NOT_LIVE_REGION", "REG_REGION_NOT_WORK_REGION",
                         "REG_CITY_NOT_LIVE_CITY", "REG_CITY_NOT_WORK_CITY", "OBS_30_CNT_SOCIAL_CIRCLE",
                         "DEF_30_CNT_SOCIAL_CIRCLE", "DAYS_LAST_PHONE_CHANGE", "previous_loan_counts"]
    cols_to_keep = categorical_columns + ordinal_columns + numerical_columns

    # # create balanced dataset to improve model performance
    print(data.shape)
    g = data.groupby("DEFAULT")
    new_data = g.apply(lambda x: x.sample(g.size().min()).reset_index(drop=True))
    print(new_data.shape)


    y = new_data["DEFAULT"]
    # remove unnecessary columns
    X = new_data[cols_to_keep]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


    # # drop NaNs
    # data = data.dropna()
    # print(data.shape)


    # create pipeline
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(sparse_output=True, handle_unknown="ignore"))
    ])
    ordinal_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder())
    ])
    numerical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    preprocessing_pipeline = ColumnTransformer([
        ("categorical_preprocessor", categorical_pipeline, categorical_columns),
        ("ordinal_preprocessor", ordinal_pipeline, ordinal_columns),
        ("numerical_preprocessor", numerical_pipeline, numerical_columns)
    ], remainder="drop")

    pipeline = Pipeline([
        ("preprocessor", preprocessing_pipeline),
        ("estimator", GradientBoostingClassifier())
    ])

    pipeline.fit(X_train, y_train)

    save_model(pipeline)
    return pipeline


if __name__ == "__main__":
    data = pd.read_csv("./data/train.csv")
    train_model(data)
