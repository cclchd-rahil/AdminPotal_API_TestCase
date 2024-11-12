# pages/base_api.py
import requests
from utils.config import BASE_URL

class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {}

    def set_authorization_token(self, token):
        # Set the authorization header with the token
        self.headers['Authorization'] = f"Bearer {token}"

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=data, headers=self.headers)

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, params=params, headers=self.headers)
