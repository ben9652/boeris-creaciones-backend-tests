import unittest
from api.network import NetworkController
from unittest.mock import patch

import api.data.RawMaterials as RawMaterialsGenerator

class TestRawMaterialController(unittest.TestCase):
    @patch('api.network.urllib3.PoolManager.request')
    def test_create_raw_materials(self, mock_request):
        mock_request.return_value.status = 200

        raw_materials = RawMaterialsGenerator.generate_raw_materials()

        for raw_material in raw_materials:
            mock_request.return_value.data = raw_material.to_json()
            raw_material.id = 0

            controller = NetworkController('http://localhost:5141/api/CatalogoMateriasPrimas')
            response = controller.post('', raw_material.to_json())
            self.assertEqual(response, mock_request.return_value.data)
