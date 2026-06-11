from api.notes.notes_api import NotesAPI
from utils.read_data import read_json


def test_update_note(headers):
    ## creaating notes
    create_payload = read_json("test_data/create_note.json")
    create_response = NotesAPI().create_note(headers, create_payload)
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]
    title_of_node = create_response.json()["data"]["title"]
    print("\n-----note created successfully-----")
    print(f"NOTE ID: {note_id}")
    print(f"NOTE TITLE: {title_of_node}")

    ## updating the created notes
    updated_payload = read_json("test_data/update_note.json")
    update_response = NotesAPI().update_note(headers, note_id, updated_payload)
    assert update_response.status_code == 200
    data = update_response.json()["data"]
    updated_title = data["title"]

    assert data["title"] == updated_payload["title"]
    assert data["description"] == updated_payload["description"]
    assert data["category"] == updated_payload["category"]

    print("\n_______updated Note__________")
    print(f"NOTE ID: {note_id}")
    print(f"NOTE TITLE: {updated_title}")

def test_update_note_invalid_id(headers):

    payload = read_json("test_data/update_note.json")
    response = NotesAPI().update_note(headers, "invalid_note_id", payload)
    print("\n--------invalid note id------------")
    print(response.status_code)
    assert response.status_code in [400,404]
