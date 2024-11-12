# pages/get_transactions_api.py
from pages.base_api import BaseAPI

class GetTransactionsAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = "/analytics/all-transaction"

    def get_all_transactions(self):
        # Use the inherited GET method with the authorization token set in BaseAPI
        return self.get(self.endpoint)
