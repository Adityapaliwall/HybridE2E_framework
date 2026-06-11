import pytest

from api.notes.notes_api import NotesAPI
from core.auth import get_auth_data
from utils.read_data import read_json


@pytest.fixture
def auth_data():
    return get_auth_data()

@pytest.fixture
def headers(auth_data):
    return { "x-auth-token": auth_data["token"] }

@pytest.fixture
# @pytest.fixture(scope="session")
def note_id(headers):

    payload = read_json("test_data/create_note.json")

    response = NotesAPI().create_note(headers, payload)
    assert response.status_code == 200
    yield response.json()["data"]["id"]