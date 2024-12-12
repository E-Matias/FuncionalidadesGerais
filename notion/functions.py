import requests
from datetime import datetime, timezone
import json

class Notion:
    def __init__(self, key_acess: str):
        self.headers = {
            "Authorization": f"Bearer {key_acess}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }

    def db_get_data(self, database_id: str, num_pages: int=None):
        page_size: int = 100 if num_pages is None else num_pages
        payload: dict = {"page_size": page_size}
        response = requests.post(f"https://api.notion.com/v1/databases/{database_id}/query", json=payload, headers=self.headers)
        print(response.status_code)
        data: dict = response.json()
        return data['results']

    def db_add_data(self, database_id: str, data: dict):
        payload: dict = {"parent": {"database_id": database_id}, "properties": data}
        result = requests.post("https://api.notion.com/v1/pages", headers=self.headers, json=payload)
        print(result.status_code)
        return result

    def db_update_data(self, row_id: str, data: dict):
        payload: dict = {"properties": data}
        result = requests.patch(f"https://api.notion.com/v1/pages/{row_id}", json=payload, headers=self.headers)
        print(result.status_code)
        return result

    def db_delete_data(self, row_id: str):
        payload: dict = {"archived": True}
        result = requests.patch(f"https://api.notion.com/v1/pages/{row_id}", json=payload, headers=self.headers)
        print(result.status_code)
        return result

    def read_note(self, page_id: str):
        result = requests.get(f"https://api.notion.com/v1/blocks/{page_id}/children", headers=self.headers)
        print(result.status_code)
        return result.json()

    def add_note_data(self, page_id: str, data: dict):
        payload: dict = {"children": data}
        response = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children", headers=self.headers, json=payload)
        print(response.status_code)
        return response

    def delete_note(self, page_id: str):
        payload: dict = {"archived": True}
        response = requests.patch(f"https://api.notion.com/v1/pages/{page_id}", headers=self.headers, json=payload)
        print(response.status_code)
        return response

    def delete_note_child(self, page_id: str):
        payload: dict = {"archived": True}
        response = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}", headers=self.headers, json=payload)
        print(response.status_code)
        return response

