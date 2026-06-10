from core.base_api import BaseAPI
from utils.config import BASE_URL


class NotesAPI:
    def __init__(self):
        self.api = BaseAPI()

    def create_note(self, headers, payload):
        return self.api.post(f"{BASE_URL}/notes", headers=headers, json=payload)

    def get_all_notes(self, headers):
        return self.api.get(f"{BASE_URL}/notes", headers=headers)

    def get_note_by_id(self, headers, note_id):
        return self.api.get(f"{BASE_URL}/notes/{note_id}", headers=headers)

    def update_note(self, headers, node_id, payload):
        return self.api.put(f"{BASE_URL}/notes/{node_id}", headers=headers, json=payload)

    def delete_note(self, headers, note_id):
        return self.api.delete(f"{BASE_URL}/notes/{note_id}", headers=headers)