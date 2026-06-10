from core.base_api import BaseAPI
from utils.config import BASE_URL


class AuthAPI:
    def __init__(self):
        self.api = BaseAPI()

    def login_user(self, payload):
        return self.api.post(f"{BASE_URL}/users/login", json = payload)

    def register_user(self, payload):
        return self.api.post(f"{BASE_URL}/users/register", json = payload)