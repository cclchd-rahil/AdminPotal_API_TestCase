# tests_api/test_get_transactions_api.py
import json

import pytest
from pages.login_api import LoginAPI
from pages.Dasboard_api.get_all_transactions import GetTransactionsAPI


@pytest.fixture
def login_api():
    api = LoginAPI()
    api.login()  # Log in to set the authorization token
    return api


@pytest.fixture
def get_transactions_api(login_api):
    return GetTransactionsAPI()  # This will use the token set by LoginAPI


def test_get_all_transactions(get_transactions_api):
    # Call the analytics endpoint
    response = get_transactions_api.get_all_transactions()

    # Print the status code and response JSON for debugging
    print("Status Code:", response.status_code)

    response_json = response.json()
    pretty_response = json.dumps(response_json, indent=4)
    print("Pretty JSON Response:\n", pretty_response)

    # Assertions to validate the response
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}. Response: {response.text}"

    # Check that expected keys are in the response JSON

