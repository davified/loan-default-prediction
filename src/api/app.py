import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


# TODO: reconcile inference-time schema (single record) with training-time schema (dataframe)
class RequestBody(BaseModel):
    Changed_Credit_Limit: float
    Payment_of_Min_Amount: float
    Credit_Mix: float
    Delay_from_due_date: float
    Annual_Income: float
    Monthly_Inhand_Salary: float
    Age: int
    Monthly_Balance: float
    Num_of_Delayed_Payment: int
    Outstanding_Debt: float
    Payment_Behaviour: float
    Credit_History_Age: float
    Num_Bank_Accounts: int
    Credit_Utilization_Ratio: float



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/predict/")
async def predict(request_body: RequestBody):
    # TODO: refactor model and API to apply preprocessing logic as well
    model = joblib.load("artifacts/model.joblib")

    # reshape request payload to a dataframe of shape (1, 14)
    df = pd.DataFrame.from_dict(request_body.dict(), orient='index')
    prediction = model.predict(df.T)

    return {"prediction": prediction.tolist()[0],
            "request": df.T.to_dict('records')[0]
            }
