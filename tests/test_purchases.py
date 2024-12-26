import unittest
import random
from api.network import NetworkController

from api.models.Rubro.RawMaterialCategory import RawMaterialCategory
from api.models.MateriasPrimas.RawMaterial import RawMaterial
from api.models.Compras.RawMaterialPurchase import RawMaterialPurchase
from api.models.Proveedor.Provider import Provider
from api.models.Usuarios.Partner import NewPartner, Partner
from api.models.Usuarios.User import User
from api.models.Compras.Purchase import Purchase
from api.models.Compras.NewPurchase import NewPurchase

import api.data.Purchases as PurchasesGenerator
import api.data.Categories as CategoriesGenerator
import api.data.RawMaterials as RawMaterialsGenerator
import api.data.Providers as ProvidersGenerator
import api.data.Partners as PartnersGenerator

class TestPurchasesController(unittest.TestCase):
    critical_failure = False

    raw_material_categories: list[int] = []
    raw_materials: list[int] = []
    providers: list[int] = []
    partners: list[int] = []
    purchases: list[int] = []
    
    def setUp(self):
        print()
    
    def test_1_create_raw_material_categories(self):
        categories: list[RawMaterialCategory] = CategoriesGenerator.generate_raw_material_categories()

        controller = NetworkController('http://localhost:5141/api/RubrosMateriasPrimas')

        for category in categories:
            try:
                new_category: RawMaterialCategory = controller.post('', category.to_json())
                TestPurchasesController.raw_material_categories.append(new_category['id'])
                print('Rubro creado exitosamente')
            except Exception as e:
                TestPurchasesController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")

    @unittest.skipIf(critical_failure, 'No se pudieron crear los rubros de materias primas')
    def test_2_create_raw_materials(self):
        controller = NetworkController('http://localhost:5141/api')

        categories_json: dict = controller.get('RubrosMateriasPrimas')
        # Filtrar los rubros de materias primas por los que se recogieron en el test anterior y asignarlos a la lista `categories`
        categories: list[RawMaterialCategory] = []
        for category in categories_json:
            if category['id'] in TestPurchasesController.raw_material_categories:
                categories.append(RawMaterialCategory.json_to_object(category))

        raw_materials: list[RawMaterial] = RawMaterialsGenerator.generate_raw_materials(20, categories)

        for raw_material in raw_materials:
            try:
                data = raw_material.to_json()
                new_raw_material: RawMaterial = controller.post('CatalogoMateriasPrimas', data)
                TestPurchasesController.raw_materials.append(new_raw_material['id'])
                print('Materia prima creada exitosamente')
            except Exception as e:
                TestPurchasesController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")
    
    @unittest.skipIf(critical_failure, 'No se pudieron crear las materias primas')
    def test_3_create_providers(self):
        controller = NetworkController('http://localhost:5141/api')

        categories_json: dict = controller.get('RubrosMateriasPrimas')
        # Filtrar los rubros de materias primas por los que se recogieron en el test anterior y asignarlos a la lista `categories`
        categories: list[RawMaterialCategory] = []
        for category in categories_json:
            if category['id'] in TestPurchasesController.raw_material_categories:
                categories.append(RawMaterialCategory.json_to_object(category))

        providers: list[Provider] = ProvidersGenerator.generate_providers(5, categories)

        for provider in providers:
            try:
                new_provider: dict = controller.post('CatalogoProveedores', provider.to_json())
                TestPurchasesController.providers.append(new_provider['id'])
                print('Proveedor creado exitosamente')
            except Exception as e:
                TestPurchasesController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")

    @unittest.skipIf(critical_failure, 'No se pudieron crear los proveedores')
    def test_4_create_partners(self):
        partners: list[NewPartner] = PartnersGenerator.generate_new_partners(2)

        controller = NetworkController('http://localhost:5141/api/Socios')

        for partner in partners:
            try:
                new_partner: dict = controller.post('', partner.to_json())
                TestPurchasesController.partners.append(new_partner['id_user'])
                print('Socio creado exitosamente')
            except Exception as e:
                TestPurchasesController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")

    @unittest.skipIf(critical_failure, 'No se pudieron crear los socios')
    def test_5_create_purchases(self):
        controller = NetworkController('http://localhost:5141/api')
        
        try:
            # Obtengo rubros de materias primas existentes
            categories_json: dict = controller.get('RubrosMateriasPrimas')
            categories: list[RawMaterialCategory] = []
            for category in categories_json:
                if(category['id'] in TestPurchasesController.raw_material_categories):
                    categories.append(RawMaterialCategory.json_to_object(category))
            
            # Obtengo materias primas existentes
            raw_materials_json: dict = controller.get('CatalogoMateriasPrimas')
            raw_materials: list[RawMaterial] = []
            for raw_material in raw_materials_json:
                if(raw_material['id'] in TestPurchasesController.raw_materials):
                    raw_materials.append(RawMaterial.json_to_object(raw_material))
            
            # Obtengo proveedores existentes
            all_providers: dict = controller.get('CatalogoProveedores')
            providers: list[Provider] = []
            for provider in all_providers:
                if provider['id'] in TestPurchasesController.providers:
                    providers.append(Provider.json_to_object(provider))
            
            # Obtengo socios existentes
            users: dict = controller.get('Socios')
            partners: list[User] = []
            # Filtrar users por la condición de que el atributo `role` sea igual a 's' y asignarlos a la lista `partners`
            for user in users:
                if user['role'] == 's' and user['id_user'] in TestPurchasesController.partners:
                    partners.append(User.json_to_object(user))

            purchases: list[NewPurchase] = []
            # Voy a seleccionar las materias primas por categoría, y por lo tanto, a los proveedores adecuados para cada una
            for raw_material_category in categories:
                selected_raw_materials: list[RawMaterialPurchase] = []
                for raw_material in raw_materials:
                    if raw_material.category.id == raw_material_category.id:
                        selected_raw_materials.append(
                            RawMaterialPurchase(
                                raw_material.id,
                                raw_material.category.id,
                                raw_material.name,
                                random.randint(1, 100),
                                random.randint(1, 1000)
                            )
                        )

                selected_providers: list[Provider] = []
                for provider in providers:
                    if provider.category.id == raw_material_category.id:
                        selected_providers.append(provider)

                if(selected_providers == [] or selected_raw_materials == [] or partners == []):
                    continue

                purchase: NewPurchase = PurchasesGenerator.generate_new_purchase(selected_providers, selected_raw_materials, partners)
                purchases.append(purchase)

            for purchase in purchases:
                response = controller.post('Compras', purchase.to_json())
                TestPurchasesController.purchases.append(response['id'])
                print('Compra creada exitosamente')
        
        except Exception as e:
            self.fail(f"El test falló debido a una excepción: {e}")

    def test_6_delete_all(self):
        controller = NetworkController('http://localhost:5141/api')

        for purchase in TestPurchasesController.purchases:
            controller.delete(f'Compras/{purchase}')
            print('Compra eliminada exitosamente')
        
        for partner in TestPurchasesController.partners:
            controller.delete(f'Socios/{partner}')
            print('Socio eliminado exitosamente')
        
        for provider in TestPurchasesController.providers:
            controller.delete(f'CatalogoProveedores/{provider}')
            print('Proveedor eliminado exitosamente')
        
        for raw_material in TestPurchasesController.raw_materials:
            controller.delete(f'CatalogoMateriasPrimas/{raw_material}')
            print('Materia prima eliminada exitosamente')

        for category in TestPurchasesController.raw_material_categories:
            controller.delete(f'RubrosMateriasPrimas/{category}')
            print('Rubro eliminado exitosamente')
