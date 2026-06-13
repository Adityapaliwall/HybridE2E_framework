from api.notes.notes_api import NotesAPI
from utils import logger
from utils.logger import get_logger

logger = get_logger(__name__)


def test_get_all_notes(headers):
    response = NotesAPI().get_all_notes(headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert isinstance(data, list)
    logger.info("\n_______Get all notes in the application________")
    logger.info(f"Total notes: {len(data)}")


def test_get_note_invalid_token():
    headers = {"x-auth-token": "invalid_token"}
    response = NotesAPI().get_all_notes(headers)
    logger.info("\n------Invalid Token-------")
    logger.info(response.status_code)
    assert response.status_code in [401,403]


def test_get_all_notes_performance(headers):
    response = NotesAPI().get_all_notes(headers)
    response_time = response.elapsed.total_seconds()
    logger.info("\n-----performance-----")
    logger.info(f"Response time: {response_time:.2f} seconds")
    assert response_time < 5