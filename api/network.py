import urllib3
import json
from typing import List, Optional

class NetworkController:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.http = urllib3.PoolManager()
    
    def request(self, method: str, endpoint: str, data: Optional[dict] = None) -> dict:
        url = f"{self.base_url}/{endpoint}"
        encoded_data = json.dumps(data).encode('utf-8') if data else None
        
        # Crear un header en el que el tipo de contenido sea JSON si es que no es None el dato. Si el tipo de dato no es JSON, poner que es texto plano.
        headers = {'Content-Type': 'application/json'} if data else {'Content-Type': 'text/plain'}

        try:
            response = self.http.request(
                method,
                url,
                headers,
                body=encoded_data
            )
            
            if response.status >= 400:
                raise Exception(f"Error {response.status}: {response.data.decode()}")
            
            # Si el tipo de dato devuelto no es un JSON, devolver el texto plano.
            if response.headers['Content-Type'] != 'application/json':
                return response.data.decode()
            return json.loads(response.data.decode())
        except Exception as e:
            raise Exception(f"Network error: {str(e)}")

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
