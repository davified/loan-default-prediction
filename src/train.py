# Basic & visualization modules
import numpy as np
import pandas as pd

# sklearn modules
from sklearn import tree
from sklearn.preprocessing import LabelEncoder as le  # label encoder
from sklearn.model_selection import train_test_split  # train & test split
from sklearn.preprocessing import RobustScaler as rbScaler  # robust scaler
from sklearn.ensemble import VotingClassifier as voClassifier  # voting
from sklearn.tree import DecisionTreeClassifier as dtClassifier  # decision tree
from sklearn.ensemble import AdaBoostClassifier as adabClassifier  # adaboosting
from sklearn.neighbors import KNeighborsClassifier as knnClassifier  # knn
from sklearn.ensemble import RandomForestClassifier as rfClassifier  # random forest
from sklearn.linear_model import LogisticRegression as lgrClassifier  # logistic regression
from sklearn.ensemble import GradientBoostingClassifier as gbClassifier  # gbm

data = pd.read_csv("./data/train.csv", encoding="utf-8", sep=",", low_memory=False)

rows = ['Age', 'Annual_Income', 'Num_of_Loan', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Outstanding_Debt',
        'Amount_invested_monthly', 'Monthly_Balance']
for row in rows:
    data[row] = data[row].str.replace(r'_+', '')

for row in rows:
    data[row] = pd.to_numeric(data[row], errors='coerce')

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

# # Modeling

x = mdf.drop(['Credit_Score'], axis=1).values
y = mdf['Credit_Score'].values

# # Split Data

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
[x_train.shape, y_train.shape]

# # Data Scaling using Robust Scaler

ro_scaler = rbScaler()
x_train = ro_scaler.fit_transform(x_train)
x_test = ro_scaler.fit_transform(x_test)
[x_train.shape, x_test.shape]

# # Random Forest Classifier

rf = rfClassifier(max_features=14, max_depth=8)

rf.fit(x_train, y_train)

rf_score = rf.score(x_train, y_train)

rf_score_t = rf.score(x_test, y_test)
print(f"model score: {rf_score_t}")
