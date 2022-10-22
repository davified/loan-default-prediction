import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rfClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler as rbScaler, LabelEncoder as le


def fit_model(x_train, y_train):
    model = rfClassifier(max_features=14, max_depth=8)
    model.fit(x_train, y_train)

    return model


def transform_data_for_training(mdf):
    x = mdf.drop(['Credit_Score'], axis=1).values
    y = mdf['Credit_Score'].values
    # # Split Data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
    # # Data Scaling using Robust Scaler
    ro_scaler = rbScaler()
    x_train = ro_scaler.fit_transform(x_train)
    x_test = ro_scaler.fit_transform(x_test)
    return x_test, x_train, y_test, y_train


def preprocess_data(data):
    rename_columns_and_convert_dtypes(data)

    # # Handle missing values
    data.dropna(thresh=26, inplace=True)
    # ## 1,744 missing Rows were removed to handle some missing values 1.7%
    data = data[['Month', 'Age', 'Occupation', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts',
                 'Num_Credit_Card', 'Interest_Rate', 'Num_of_Loan', 'Type_of_Loan',
                 'Delay_from_due_date', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit',
                 'Num_Credit_Inquiries', 'Credit_Mix', 'Outstanding_Debt',
                 'Credit_Utilization_Ratio', 'Credit_History_Age',
                 'Payment_of_Min_Amount', 'Total_EMI_per_month',
                 'Amount_invested_monthly', 'Payment_Behaviour', 'Monthly_Balance',
                 'Credit_Score']]
    data.dropna(thresh=24, inplace=True)
    # # Encode categorical values
    data.select_dtypes(['object']).columns
    Month_le = le()
    Occupation_le = le()
    Type_of_Loan_le = le()
    Credit_Mix_le = le()
    Credit_History_Age_le = le()
    Payment_of_Min_Amount_le = le()
    Payment_Behaviour_le = le()
    Credit_Score_le = le()
    data['Month'] = Month_le.fit_transform(data['Month'])
    data['Occupation'] = Occupation_le.fit_transform(data['Occupation'])
    data['Type_of_Loan'] = Type_of_Loan_le.fit_transform(data['Type_of_Loan'])
    data['Credit_Mix'] = Credit_Mix_le.fit_transform(data['Credit_Mix'])
    data['Credit_History_Age'] = Credit_History_Age_le.fit_transform(data['Credit_History_Age'])
    data['Payment_of_Min_Amount'] = Payment_of_Min_Amount_le.fit_transform(data['Payment_of_Min_Amount'])
    data['Payment_Behaviour'] = Payment_Behaviour_le.fit_transform(data['Payment_Behaviour'])
    data['Credit_Score'] = Credit_Score_le.fit_transform(data['Credit_Score'])
    mdf = data[['Credit_Score', 'Changed_Credit_Limit', 'Payment_of_Min_Amount', 'Credit_Mix', 'Delay_from_due_date',
                'Annual_Income', 'Monthly_Inhand_Salary', 'Age', 'Monthly_Balance', 'Num_of_Delayed_Payment',
                'Outstanding_Debt', 'Payment_Behaviour', 'Credit_History_Age', 'Num_Bank_Accounts',
                'Credit_Utilization_Ratio']]

    return mdf


def rename_columns_and_convert_dtypes(data):
    columns = ['Age', 'Annual_Income', 'Num_of_Loan', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit',
               'Outstanding_Debt',
               'Amount_invested_monthly', 'Monthly_Balance']
    for col in columns:
        data[col] = data[col].str.replace(r'_+', '')
    for col in columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')


def evaluate_model(model, x_test, x_train, y_test, y_train):
    rf_score = model.score(x_train, y_train)
    rf_score_test = model.score(x_test, y_test)

    return rf_score_test


def save_model(model):
    target_directory = "artifacts"
    os.makedirs(target_directory, exist_ok=True)
    joblib.dump(model, f"{target_directory}/model.joblib")
