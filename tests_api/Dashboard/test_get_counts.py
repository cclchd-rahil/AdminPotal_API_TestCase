# tests_api/test_counts_api.py
import json

import pytest
from pages.login_api import LoginAPI
from pages.Dasboard_api.get_counts_api import CountsAPI


@pytest.fixture(scope="session")
def login_and_set_token():
    login_api = LoginAPI()
    login_api.login()  # Logs in and sets the authorization token
    return login_api


@pytest.fixture
def counts_api(login_and_set_token):
    # Pass the token to CountsAPI after login
    return CountsAPI()


def test_get_counts(counts_api):
    response = counts_api.get_counts()

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}. Response: {response.text}"

    data = response.json()
    print("Counts Data:", json.dumps(data, indent=4))

    # Example validations on the counts data
    assert "adminCount" in data, "adminCount missing from response"
    assert "vendorCount" in data, "vendorCount missing from response"
    assert "operatorCount" in data, "operatorCount missing from response"
    assert "transactionCount" in data, "transactionCount missing from response"
