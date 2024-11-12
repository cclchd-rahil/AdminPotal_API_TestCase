# pages/login_api.py
from pages.base_api import BaseAPI
from utils.config import LOGIN_CREDENTIALS

class LoginAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = "/admins/login"  # Update this to the actual login endpoint

    def login(self):
        # Using the credentials directly from the config
        payload = LOGIN_CREDENTIALS
        return self.post(self.endpoint, data=payload)
