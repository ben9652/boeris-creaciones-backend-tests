import unittest
from api.network import NetworkController
from unittest.mock import patch

class TestNetworkController(unittest.TestCase):
    @patch('api.network.urllib3.PoolManager.request')
    def test_get_success(self, mock_request):
        mock_request.return_value.status = 200
        mock_request.return_value.data = b'Bienvenido al controlador de usuarios'

        controller = NetworkController('http://localhost:5141/api/Usuarios')
        response = controller.get('/Testing')
        self.assertEqual(response, 'Bienvenido al controlador de usuarios')
    
    @patch('api.network.urllib3.PoolManager.request')
    def test_get_error(self, mock_request):
        mock_request.return_value.status = 404
        mock_request.return_value.data = b'{"error": "Resource not found"}'
        controller = NetworkController('http://localhost:5141/api')
        with self.assertRaises(Exception) as context:
            controller.get('/EndpointNoExistente')
        self.assertTrue(str(context.exception).startswith("Network error"))
