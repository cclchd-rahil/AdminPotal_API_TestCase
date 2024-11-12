# tests_api/test_login_api.py
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
    json_str = json.dumps(json_data, indent=4)
    print("JSON Response Body:\n", json_str)

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}. Response: {response.text}"

    assert "token" in response.json()

def test_login_missing_password(login_api):

    login_data = {
        "email": "superadmin@gmail.com",
        "rememberMe": True
    }
    response = login_api.login(login_data)

    print("Status Code:", response.status_code)
    print("Response Data:", response.json())

    # Check if the response code is 400 (Bad Request)
    assert response.status_code == 400, f"Expected 400 but got {response.status_code}. Response: {response.text}"
