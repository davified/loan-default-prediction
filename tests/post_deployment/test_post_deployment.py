import pytest
import requests


@pytest.mark.skip(reason="Placeholder. Skipping for now as we don't have a deployed API instance yet")
class TestPostDeployment:
    endpoint_url = "https://my-model-api.example.com"

    def test_root(self):
        response = requests.get(self.endpoint_url)

        assert response.status_code == 200

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

        response = requests.post(f"{self.endpoint_url}/predict/", headers={"Content-Type": "application/json"},
                                 json=valid_request_payload,
                                 )

        assert response.status_code == 200
