from api.notes.notes_api import NotesAPI
from utils.read_data import read_json
from utils import logger
from utils.logger import get_logger

logger = get_logger(__name__)


def test_delete_note(headers):

## creating the node
    create_payload = read_json("test_data/create_note.json")
    create_response = NotesAPI().create_note(headers,create_payload)
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]
    print("\n-------- NOTE CREATED ---------")
    logger.info("\n-------- NOTE CREATED ---------")
    logger.info(f"Note ID : {note_id}")

## deleting the nodes
    delete_response = NotesAPI().delete_note(headers,note_id)
    assert delete_response.status_code == 200
    logger.info("\n===== NOTE DELETED =====")
    logger.info(f"Deleted Note ID : {note_id}")
    get_response = NotesAPI().get_note_by_id(headers,note_id)
    assert get_response.status_code in [400, 404]
    logger.info("Deleted Note Not Found")

def test_delete_note_invalid_id(headers):

    response = NotesAPI().delete_note(headers,"invalid_id")
    logger.info("\n===== INVALID NOTE ID =====")
    logger.info(response.status_code)
    assert response.status_code in [400, 404]