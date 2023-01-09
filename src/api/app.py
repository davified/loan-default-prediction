import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


# TODO: reconcile inference-time schema (single record) with training-time schema (dataframe)
from training.training_helpers import load_model


class RequestBody(BaseModel):
    CONTRACT_TYPE: str
    GENDER: str
    FLAG_OWN_CAR: str
    FLAG_OWN_REALTY: str
    COUNT_CHILDREN: float
    INCOME: float
    AMT_CREDIT: float
    AMT_ANNUITY: float
    NAME_TYPE_SUITE: str
    INCOME_TYPE: str
    EDUCATION_TYPE: str
    FAMILY_STATUS: str
    HOUSING_TYPE: str
    REGION_POPULATION_RELATIVE: float
    DAYS_BIRTH: int
    DAYS_EMPLOYED: int
    DAYS_REGISTRATION: int
    DAYS_ID_PUBLISH: float
    OCCUPATION_TYPE: str
    REGION_RATING_CLIENT: int
    WEEKDAY_APPR_PROCESS_START: str
    HOUR_APPR_PROCESS_START: float
    REG_REGION_NOT_LIVE_REGION: float
    REG_REGION_NOT_WORK_REGION: float
    REG_CITY_NOT_LIVE_CITY: float
    REG_CITY_NOT_WORK_CITY: float
    ORGANIZATION_TYPE: str
    OBS_30_CNT_SOCIAL_CIRCLE: float
    DEF_30_CNT_SOCIAL_CIRCLE: float
    DAYS_LAST_PHONE_CHANGE: float
    previous_loan_counts: int



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/predict/")
async def predict(request_body: RequestBody):
    pipeline = load_model()

    # reshape request payload to a dataframe
    df = pd.DataFrame.from_dict(request_body.dict(), orient="index")
    prediction = pipeline.predict(df.T)

    return {"prediction": prediction.tolist()[0],
            "request": df.T.to_dict("records")[0]
            }
