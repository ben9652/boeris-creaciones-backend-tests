import requests
from typing import List, Optional
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class NetworkController:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def request(self, method: str, endpoint: str, data: Optional[dict] = None) -> dict:
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'} if data else {'Content-Type': 'text/plain'}

        # Cómo se hace una estructura 'switch'
        response = None
        if method == 'GET':
            response = requests.get(url, headers=headers, verify=False)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=data, verify=False)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, json=data, verify=False)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers, verify=False)
        elif method == 'PATCH':
            response = requests.patch(url, headers=headers, json=data, verify=False)
        
        if response.status_code >= 400:
            raise Exception(f"Error {response.status_code}: {response.text}")

        if 'application/json' not in response.headers.get('Content-Type', ''):
            return response.text
        return response.json()

    def get(self, endpoint: str) -> dict:
        return self.request('GET', endpoint)
    
    def post(self, endpoint: str, data: dict) -> dict:
        return self.request('POST', endpoint, data)
    
    def put(self, endpoint: str, data: dict) -> dict:
        return self.request('PUT', endpoint, data)
    
    def delete(self, endpoint: str) -> dict:
        return self.request('DELETE', endpoint)
    
    def validate_patch_document(self, patch_document: List[dict]):
        """Validates the JSON Patch document"""
        valid_ops = ['add', 'remove', 'replace', 'move', 'copy', 'test']
        for operation in patch_document:
            if not isinstance(operation, dict):
                raise ValueError('Each operation must be a dictionary.')
            if 'op' not in operation or operation['op'] not in valid_ops:
                raise ValueError(f"Invalid operation: {operation.get('op')}")
            if 'path' not in operation:
                raise ValueError('Each operation must have a path.')
            if operation['op'] in ['add', 'replace', 'test'] and 'value' not in operation:
                raise ValueError(f"Operation {operation['op']} must include a 'value' key.")

    def patch(self, endpoint: str, patch_document: list) -> dict:
        """
        Sends a PATCH request with a JSON Patch document.

        :param endpoint: API endpoint (e.g., '/resource/1').
        :param patch_document: A list of JSON Patch operations (e.g., [{'op': 'replace', 'path': '/field', 'value': 'new_value'}]).
        """
        self.validate_patch_document(patch_document)
        return self.request(
            'PATCH',
            endpoint,
            data=patch_document
        )