# api_tests/test_login_api.py
import json

import pytest
from pages.login_api import LoginAPI

@pytest.fixture
def login_api():
    return LoginAPI()

def test_login_success(login_api):
    # Call the login method, which will use config-based credentials
    response = login_api.login()

    print("Status Code:", response.status_code)
    print("Response Data:", response.json())

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)  # Use json.dumps() instead of json.dump()
    print("JSON Response Body:\n", json_str)

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}. Response: {response.text}"
    # Additional assertions to validate response structure and content
    assert "token" in response.json()  # Example: check if login token is in response
