from fastapi.testclient import TestClient
from precisely import (any_of, assert_that, equal_to, is_mapping)

from api.app import app

client = TestClient(app)


class TestApp():
    def test_root(self):
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {"message": "hello world"}

    def test_predict_should_return_a_prediction_when_given_a_valid_payload(self):
        valid_request_payload = {"CONTRACT_TYPE": "Cash loans",
                                 "GENDER": "M",
                                 "FLAG_OWN_CAR": "N",
                                 "FLAG_OWN_REALTY": "Y",
                                 "COUNT_CHILDREN": 0,
                                 "INCOME": 202500.0,
                                 "AMT_CREDIT": 406597.5,
                                 "AMT_ANNUITY": 24700.5,
                                 "NAME_TYPE_SUITE": "Unaccompanied",
                                 "INCOME_TYPE": "Working",
                                 "EDUCATION_TYPE": "Secondary / secondary special",
                                 "FAMILY_STATUS": "Single / not married",
                                 "HOUSING_TYPE": "House / apartment",
                                 "REGION_POPULATION_RELATIVE": 0.018801,
                                 "DAYS_BIRTH": -9461,
                                 "DAYS_EMPLOYED": -637,
                                 "DAYS_REGISTRATION": -3648,
                                 "DAYS_ID_PUBLISH": -2120,
                                 "OCCUPATION_TYPE": "Laborers",
                                 "REGION_RATING_CLIENT": 2,
                                 "WEEKDAY_APPR_PROCESS_START": "WEDNESDAY",
                                 "HOUR_APPR_PROCESS_START": 10,
                                 "REG_REGION_NOT_LIVE_REGION": 0,
                                 "REG_REGION_NOT_WORK_REGION": 0,
                                 "REG_CITY_NOT_LIVE_CITY": 0,
                                 "REG_CITY_NOT_WORK_CITY": 0,
                                 "ORGANIZATION_TYPE": "Business Entity Type 3",
                                 "OBS_30_CNT_SOCIAL_CIRCLE": 2.0,
                                 "DEF_30_CNT_SOCIAL_CIRCLE": 2.0,
                                 "DAYS_LAST_PHONE_CHANGE": -1134.0,
                                 "previous_loan_counts": 8,
                                 }

        response = client.post("/predict/", headers={"Content-Type": "application/json"},
                               json=valid_request_payload,
                               )

        assert response.status_code == 200
        assert_that(response.json(), is_mapping({"prediction": any_of(equal_to(0), equal_to(1)),
                                                 "request": valid_request_payload})
                    )
