from api.notes.notes_api import NotesAPI
from utils.read_data import read_json


def test_delete_note(headers):

## creating the node
    create_payload = read_json("test_data/create_note.json")
    create_response = NotesAPI().create_note(headers,create_payload)
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]
    print("\n-------- NOTE CREATED ---------")
    print(f"Note ID : {note_id}")

## deleting the nodes
    delete_response = NotesAPI().delete_note(headers,note_id)
    assert delete_response.status_code == 200
    print("\n===== NOTE DELETED =====")
    print(f"Deleted Note ID : {note_id}")
    get_response = NotesAPI().get_note_by_id(headers,note_id)
    assert get_response.status_code in [400, 404]
    print("Deleted Note Not Found")

def test_delete_note_invalid_id(headers):

    response = NotesAPI().delete_note(headers,"invalid_id")
    print("\n===== INVALID NOTE ID =====")
    print(response.status_code)
    assert response.status_code in [400, 404]