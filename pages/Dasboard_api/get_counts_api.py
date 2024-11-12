# pages/counts_api.py
from pages.base_api import BaseAPI

class CountsAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = "/analytics/"

    def get_counts(self):
        return self.get(self.endpoint)
