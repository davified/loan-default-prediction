import pytest
import requests


@pytest.mark.skip(reason="Placeholder. Skipping for now as we don't have a deployed API instance yet")
class TestPostDeployment:
    endpoint_url = "https://my-model-api.example.com"

    def test_root(self):
        response = requests.get(self.endpoint_url)

        assert response.status_code == 200

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

        response = requests.post(f"{self.endpoint_url}/predict/", headers={"Content-Type": "application/json"},
                                 json=valid_request_payload,
                                 )

        assert response.status_code == 200
