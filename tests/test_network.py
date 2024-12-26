import unittest
from api.network import NetworkController

class TestNetworkController(unittest.TestCase):
    def test_1_get_success(self):
        controller = NetworkController('http://localhost:5141/api/Usuarios')
        response = controller.get('Testing')
        self.assertEqual(response, 'Bienvenido al controlador de usuarios')
    
    def test_2_get_error(self):
        controller = NetworkController('http://localhost:5141/api')
        with self.assertRaises(Exception) as context:
            controller.get('/EndpointNoExistente')
        self.assertTrue(str(context.exception).startswith("Error"))
