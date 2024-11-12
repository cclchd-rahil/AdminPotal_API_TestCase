# pages/base_api.py
import requests
from utils.config import BASE_URL

class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, headers=None):
        response = requests.get(f"{self.base_url}{endpoint}", headers=headers)
        return response

    def post(self, endpoint, data=None, headers=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=data, headers=headers)
        return response
