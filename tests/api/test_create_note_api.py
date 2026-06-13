from api.notes.notes_api import NotesAPI
from utils.read_data import read_json
import allure
from utils import logger
from utils.logger import get_logger

logger = get_logger(__name__)


@allure.feature("Notes API")
@allure.story("Create Note - Positive")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_note(headers):

    payload = read_json("test_data/create_note.json")

    response = NotesAPI().create_note(headers, payload)

    assert response.status_code == 200

    data = response.json()["data"]

    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["category"] == payload["category"]

    logger.info("\n----------------Note created successfully-------------")


@allure.feature("Notes API")
@allure.story("Create Note - Negative")
@allure.severity(allure.severity_level.NORMAL)
def test_create_note_invalid_data(headers):

    payload = read_json("test_data/create_note_invalid.json")

    response = NotesAPI().create_note(headers, payload)

    logger.info("\n-------Invalid note below are status code------")
    logger.info(response.status_code)
    logger.info(response.text)

    assert response.status_code in [400, 422]