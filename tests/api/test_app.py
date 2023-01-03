import unittest

from fastapi.testclient import TestClient
from precisely import assert_that, is_mapping, greater_than_or_equal_to, less_than_or_equal_to

from api.app import app

client = TestClient(app)


class TestApp(unittest.TestCase):
    def test_root(self):
        response = client.get("/")

        self.assertEqual(200, response.status_code)
        self.assertEqual({"message": "hello world"}, response.json())

    def test_predict_should_return_a_prediction_when_given_a_valid_payload(self):
        valid_request_payload = {
            "Changed_Credit_Limit": 0,
            "Payment_of_Min_Amount": 0,
            "Credit_Mix": 0,
            "Delay_from_due_date": 0,
            "Annual_Income": 0,
            "Monthly_Inhand_Salary": 0,
            "Age": 0,
            "Monthly_Balance": 0,
            "Num_of_Delayed_Payment": 0,
            "Outstanding_Debt": 0,
            "Payment_Behaviour": 0,
            "Credit_History_Age": 0,
            "Num_Bank_Accounts": 0,
            "Credit_Utilization_Ratio": 0
        }
        response = client.post("/predict/", headers={"Content-Type": "application/json"},
                               json=valid_request_payload,
                               )

        self.assertEqual(200, response.status_code)
        assert_that(response.json(), is_mapping({"prediction": greater_than_or_equal_to(0) and less_than_or_equal_to(4),
                                                 "request": valid_request_payload})
                    )
