# pages/login_api.py
from pages.base_api import BaseAPI
from utils.config import LOGIN_CREDENTIALS


class LoginAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = "/admins/login"  # Update this to the actual login endpoint

    def login(self, payload=None):
        if payload is None:
            payload = LOGIN_CREDENTIALS

        response = self.post(self.endpoint, data=payload)

        # Check if login was successful and set the authorization token
        if response.status_code == 200:
            token = response.json().get("token")
            if token:
                self.set_authorization_token(token)  # Store token for future requests
        else:
            print(f"Login failed with status code {response.status_code}")

        return response
