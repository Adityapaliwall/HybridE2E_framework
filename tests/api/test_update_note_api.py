from api.notes.notes_api import NotesAPI
from utils.read_data import read_json
from utils import logger
from utils.logger import get_logger

logger = get_logger(__name__)


def test_update_note(headers):
    ## creaating notes
    create_payload = read_json("test_data/create_note.json")
    create_response = NotesAPI().create_note(headers, create_payload)
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]
    title_of_node = create_response.json()["data"]["title"]
    logger.info("\n-----note created successfully-----")
    logger.info(f"NOTE ID: {note_id}")
    logger.info(f"NOTE TITLE: {title_of_node}")

    ## updating the created notes
    updated_payload = read_json("test_data/update_note.json")
    update_response = NotesAPI().update_note(headers, note_id, updated_payload)
    assert update_response.status_code == 200
    data = update_response.json()["data"]
    updated_title = data["title"]

    assert data["title"] == updated_payload["title"]
    assert data["description"] == updated_payload["description"]
    assert data["category"] == updated_payload["category"]

    logger.info("\n_______updated Note__________")
    logger.info(f"NOTE ID: {note_id}")
    logger.info(f"NOTE TITLE: {updated_title}")

def test_update_note_invalid_id(headers):

    payload = read_json("test_data/update_note.json")
    response = NotesAPI().update_note(headers, "invalid_note_id", payload)
    logger.info("\n--------invalid note id------------")
    logger.info(response.status_code)
    assert response.status_code in [400,404]
