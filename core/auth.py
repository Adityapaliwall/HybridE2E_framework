from api.authentication.auth_api import AuthAPI
from utils.read_data import read_json


def get_auth_data():

    payload = read_json("test_data/login.json")

    response = AuthAPI().login_user(payload)

    token = response.json()["data"]["token"]

    return { "token": token}