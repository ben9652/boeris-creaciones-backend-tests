import unittest
import random
from api.network import NetworkController

from api.models.Rubro.RawMaterialCategory import RawMaterialCategory
from api.models.MateriasPrimas.RawMaterial import RawMaterial
from api.models.Compras.RawMaterialPurchase import RawMaterialPurchase
from api.models.Usuarios.User import User
from api.models.Sucursal.Branch import Branch
from api.models.Sucursal.Locality import Locality
from api.models.Sucursal.Province import Province
from api.models.Compras.NewPurchase import NewPurchase
from api.models.Compras.Purchase import ReceivePurchase
from api.models.Usuarios.Partner import NewPartner
from api.models.Proveedor.Provider import Provider

from api.models.MateriasPrimas.RawMaterial import RawMaterialManufacture
from api.models.MateriasPrimas.RawMaterial import ManufactureRawMaterial
from api.models.MateriasPrimas.RawMaterial import StoredRawMaterial

import api.data.Purchases as PurchasesGenerator
import api.data.Categories as CategoriesGenerator
import api.data.RawMaterials as RawMaterialsGenerator
import api.data.Providers as ProvidersGenerator
import api.data.Partners as PartnersGenerator
import api.data.Branches as BranchesGenerator

import paramiko

import winsound
FRECUENCY = 1560
DURATION = 1000

class Elaboration:
    def __init__(self, id_raw_material: int, id_branch: int):
        self.id_raw_material = id_raw_material
        self.id_branch = id_branch

class TestManufactureRawMaterialsController(unittest.TestCase):
    critical_failure = False

    raw_material_categories: list[int] = []
    raw_materials: list[int] = []
    providers: list[int] = []
    partners: list[int] = []
    purchases: list[int] = []
    localities: list[int] = []
    branches: list[int] = []
    # Declarar una lista para almacenar, en un tipo de dato con dos atributos, elaboraciones
    elaborations: list[Elaboration] = []

    def setUp(self):
        print()
    
    def test_1(self):
        self.assertTrue(True, "Este test es un placeholder y siempre pasa.")
    
    def test_1_create_raw_material_categories(self):
        categories: list[RawMaterialCategory] = CategoriesGenerator.generate_raw_material_categories()

        controller = NetworkController('http://localhost:5141/api/RubrosMateriasPrimas')

        for category in categories:
            try:
                new_category: RawMaterialCategory = controller.post('', category.to_json())
                TestManufactureRawMaterialsController.raw_material_categories.append(new_category['id'])
                print('Rubro creado exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                TestManufactureRawMaterialsController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")
    
    @unittest.skipIf(critical_failure, 'No se pudieron crear los rubros de materias primas')
    def test_2_create_raw_materials(self):
        controller = NetworkController('http://localhost:5141/api')

        categories_json: dict = controller.get('RubrosMateriasPrimas')
        # Filtrar los rubros de materias primas por los que se recogieron en el test anterior y asignarlos a la lista `categories`
        categories: list[RawMaterialCategory] = []
        for category in categories_json:
            if category['id'] in TestManufactureRawMaterialsController.raw_material_categories:
                categories.append(RawMaterialCategory.json_to_object(category))

        raw_materials: list[RawMaterial] = RawMaterialsGenerator.generate_raw_materials(20, categories)

        for raw_material in raw_materials:
            try:
                data = raw_material.to_json()
                new_raw_material: RawMaterial = controller.post('CatalogoMateriasPrimas', data)
                TestManufactureRawMaterialsController.raw_materials.append(new_raw_material['id'])
                print('Materia prima creada exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                TestManufactureRawMaterialsController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")
                
    @unittest.skipIf(critical_failure, 'No se pudieron crear las materias primas')
    def test_3_create_providers(self):
        controller = NetworkController('http://localhost:5141/api')

        categories_json: dict = controller.get('RubrosMateriasPrimas')
        # Filtrar los rubros de materias primas por los que se recogieron en el test anterior y asignarlos a la lista `categories`
        categories: list[RawMaterialCategory] = []
        for category in categories_json:
            if category['id'] in TestManufactureRawMaterialsController.raw_material_categories:
                categories.append(RawMaterialCategory.json_to_object(category))
        
        providers: list[User] = ProvidersGenerator.generate_providers(5, categories)

        for provider in providers:
            try:
                data = provider.to_json()
                new_provider: User = controller.post('CatalogoProveedores', data)
                TestManufactureRawMaterialsController.providers.append(new_provider['id'])
                print('Proveedor creado exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                TestManufactureRawMaterialsController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")
    
    @unittest.skipIf(critical_failure, 'No se pudieron crear los proveedores')
    def test_4_create_partners(self):
        controller = NetworkController('http://localhost:5141/api')

        partners: list[NewPartner] = PartnersGenerator.generate_new_partners(4)

        for partner in partners:
            try:
                new_partner: User = controller.post('Socios', partner.to_json())
                TestManufactureRawMaterialsController.partners.append(new_partner['id_user'])
                print('Socio creado exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                TestManufactureRawMaterialsController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")
    
    @unittest.skipIf(critical_failure, 'No se pudieron crear los socios')
    def test_5_create_localities(self):
        controller = NetworkController('http://localhost:5141/api')

        # Generar localidades
        localities: list[Locality] = BranchesGenerator.generate_localities(5)
        
        for locality in localities:
            try:
                data = locality.to_json()
                new_locality: Locality = controller.post('Localidades', data)
                TestManufactureRawMaterialsController.localities.append(new_locality['id'])
                print('Localidad creada exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                TestManufactureRawMaterialsController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")

    @unittest.skipIf(critical_failure, 'No se pudieron crear los socios')
    def test_6_create_branches(self):
        controller = NetworkController('http://localhost:5141/api')

        localities_json: dict = controller.get('Localidades')
        # Filtrar las localidades por las que se recogieron en el test anterior y asignarlos a la lista `localities`
        localities: list[Locality] = []
        for locality in localities_json:
            if locality['id'] in TestManufactureRawMaterialsController.localities:
                localities.append(Locality.json_to_object(locality))

        branches: list[Branch] = BranchesGenerator.generate_branches(5, localities)

        for branch in branches:
            try:
                data = branch.to_json()
                new_branch: Branch = controller.post('CatalogoSucursales', data)
                TestManufactureRawMaterialsController.branches.append(new_branch['id'])
                print('Sucursal creada exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                TestManufactureRawMaterialsController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")
    
    @unittest.skipIf(critical_failure, 'No se pudieron crear las sucursales')
    def test_7_create_purchases(self):
        controller = NetworkController('http://localhost:5141/api')

        try:
            # Obtengo rubros de materias primas existentes
            categories_json: dict = controller.get('RubrosMateriasPrimas')
            categories: list[RawMaterialCategory] = []
            for category in categories_json:
                if(category['id'] in TestManufactureRawMaterialsController.raw_material_categories):
                    categories.append(RawMaterialCategory.json_to_object(category))
            
            # Obtengo materias primas existentes
            raw_materials_json: dict = controller.get('CatalogoMateriasPrimas')
            raw_materials: list[RawMaterial] = []
            for raw_material in raw_materials_json:
                if(raw_material['id'] in TestManufactureRawMaterialsController.raw_materials):
                    raw_materials.append(RawMaterial.json_to_object(raw_material))
            
            # Obtengo proveedores existentes
            providers_json: dict = controller.get('CatalogoProveedores')
            providers: list[Provider] = []
            for provider in providers_json:
                if provider['id'] in TestManufactureRawMaterialsController.providers:
                    providers.append(Provider.json_to_object(provider))
            
            # Obtengo socios existentes
            partners_json: dict = controller.get('Socios')
            partners: list[User] = []
            # Filtrar partners_json por la condición de que el atributo `role` sea igual a 's' y asignarlos a la lista `partners`
            for partner in partners_json:
                if partner['role'] == 's' and partner['id_user'] in TestManufactureRawMaterialsController.partners:
                    partners.append(User.json_to_object(partner))
            
            # Obtengo sucursales existentes
            branches_json: dict = controller.get('CatalogoSucursales')
            branches: list[Branch] = []
            for branch in branches_json:
                if branch['id'] in TestManufactureRawMaterialsController.branches:
                    branches.append(Branch.json_to_object(branch))
            
            purchases: list[NewPurchase] = []
            # Voy a seleccionar las materias primas por categoría, y por lo tanto, a los proveedores adecuados para cada una
            for raw_material_category in categories:
                selected_raw_materials: list[RawMaterial] = []
                for raw_material in raw_materials:
                    if raw_material.category.id == raw_material_category.id:
                        selected_raw_materials.append(
                            RawMaterialPurchase(
                                raw_material.id,
                                raw_material.category,
                                raw_material.name,
                                random.randint(1, 100),
                                random.randint(1, 1000)
                            )
                        )
                        
                selected_providers: list[Provider] = []
                for provider in providers:
                    if provider.category.id == raw_material_category.id:
                        selected_providers.append(provider)
                
                if (selected_providers == [] or selected_raw_materials == [] or partners == []):
                    continue
                    
                purchase: NewPurchase = PurchasesGenerator.generate_new_purchase(selected_providers, selected_raw_materials, partners)
                purchases.append(purchase)
            
            for purchase in purchases:
                response = controller.post('Compras', purchase.to_json())
                TestManufactureRawMaterialsController.purchases.append(response['id'])
                print('Compra creada exitosamente')
        
        except Exception as e:
            winsound.Beep(FRECUENCY, DURATION)
            TestManufactureRawMaterialsController.critical_failure = True
            self.fail(f"El test falló debido a una excepción: {e}")

    @unittest.skipIf(critical_failure, 'No se pudieron crear las compras')
    def test_8_receive_purchases(self):
        controller = NetworkController('http://localhost:5141/api')

        for purchase_id in TestManufactureRawMaterialsController.purchases:
            try:
                # Obtengo aleatoriamente un ID de un socio de los que se crearon
                partner_id = random.choice(TestManufactureRawMaterialsController.partners)

                # Obtengo aleatoriamente un ID de una sucursal de las que se crearon
                branch_id = random.choice(TestManufactureRawMaterialsController.branches)
                
                receiveObj: ReceivePurchase = ReceivePurchase(branch_id, 0.0)
                response = controller.post(f'Compras/recibir/{purchase_id}-{partner_id}', receiveObj.to_json())
                print('Compra recibida exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                TestManufactureRawMaterialsController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")
    
    @unittest.skipIf(critical_failure, 'No se pudieron recibir las compras')
    def test_9_elaborate_raw_materials(self):
        controller = NetworkController('http://localhost:5141/api')

        for i in range(10):
            try:
                # Obtengo aleatoriamente un ID de una materia prima de las que se crearon
                raw_material_id = random.choice(TestManufactureRawMaterialsController.raw_materials)

                # Obtengo aleatoriamente un ID de una sucursal de las que se crearon
                branch_id = random.choice(TestManufactureRawMaterialsController.branches)

                # Obtengo aleatoriamente un ID de un socio de los que se crearon
                partner_id = random.choice(TestManufactureRawMaterialsController.partners)

                # Obtengo todas las materias primas
                raw_materials_json: dict = controller.get('CatalogoMateriasPrimas/almacenadas')
                # Filtrar las materias primas por las que se recogieron en el test anterior y asignarlos a la lista `raw_materials`
                raw_materials: list[StoredRawMaterial] = []
                for raw_material in raw_materials_json:
                    if raw_material['id'] in TestManufactureRawMaterialsController.raw_materials and raw_material['stock'] > 0 and raw_material['branch']['id'] == branch_id:
                        raw_materials.append(StoredRawMaterial.json_to_object(raw_material))
                
                if (raw_materials == []):
                    continue

                # Creo las materias primas que se usarán para la elaboración
                materials: list[ManufactureRawMaterial] = []
                for j in range(random.randint(1, 5)):
                    raw_material: StoredRawMaterial = random.choice(raw_materials)
                    stock_in_branch: int = raw_material.stock_in_branch
                    # Si el ID de materia prima ya está en la lista, no lo agrego
                    if any(material.id_raw_material == raw_material.id for material in materials):
                        continue
                    materials.append(ManufactureRawMaterial(raw_material.id, raw_material.stock, stock_in_branch, random.randint(0, stock_in_branch)))
                
                # Genero la elaboración de la materia prima
                elaboration: RawMaterialManufacture = RawMaterialManufacture(raw_material_id, random.randint(1, 2), partner_id, branch_id, materials)
                
                response = controller.post('ElaboracionMateriasPrimas', elaboration.to_json())
                TestManufactureRawMaterialsController.elaborations.append(Elaboration(response['id'], branch_id))
                print('Materia prima elaborada exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                TestManufactureRawMaterialsController.critical_failure = True
                self.fail(f"El test falló debido a una excepción: {e}")

    @classmethod
    def tearDownClass(self):
        controller = NetworkController('http://localhost:5141/api')
        print()

#        try:
#            ssh = paramiko.SSHClient()
#            ssh.load_system_host_keys()
#            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#            ssh.connect('boeris.zapto.org', 22, 'ubuntu', key_filename='C:\\Users\\bboeri\\Documents\\Publish\\BoerisKeys.pem')
#            stdin, stdout, stderr = ssh.exec_command('/home/ubuntu/backupDatabase.sh')
#            if stderr.read():
#                raise Exception(f"Error al hacer el backup de la base de datos: {stderr.read().decode()}")
#            ssh.close()
#        except Exception as e:
#            winsound.Beep(FRECUENCY, DURATION)
#            self.fail(f"El test falló debido a una excepción al intentar hacer el backup de la base de datos: {e}")

        ############## OBTENCIÓN DE DATOS PARA ELIMINARLOS ##############

#        # Se obtienen los datos de las elaboraciones para poder eliminarlas
#        raw_materials_json: dict = controller.get('ElaboracionMateriasPrimas/elaboraciones')
#        for raw_material in raw_materials_json:
#            TestManufactureRawMaterialsController.elaborations.append(Elaboration(raw_material['elaborated_raw_materials'][0]['raw_material']['id'], raw_material['branch']['id']))
#
#        # Se obtienen los datos de los socios para poder eliminarlos
#        partners_json: dict = controller.get('Socios')
#        for partner in partners_json:
#            TestManufactureRawMaterialsController.partners.append(partner['id_user'])
#        
#        # Se obtienen los datos de las compras para poder eliminarlas
#        purchases_json: dict = controller.get('Compras')
#        for purchase in purchases_json:
#            TestManufactureRawMaterialsController.purchases.append(purchase['id'])
#        
#        # Se obtienen los datos de las sucursales para poder eliminarlas
#        branches_json: dict = controller.get('CatalogoSucursales')
#        for branch in branches_json:
#            TestManufactureRawMaterialsController.branches.append(branch['id'])
#        
#        # Se obtienen los datos de las localidades para poder eliminarlas
#        localities_json: dict = controller.get('Localidades')
#        for locality in localities_json:
#            TestManufactureRawMaterialsController.localities.append(locality['id'])
#
#        # Se obtienen los datos de los proveedores para poder eliminarlos
#        providers_json: dict = controller.get('CatalogoProveedores')
#        for provider in providers_json:
#            TestManufactureRawMaterialsController.providers.append(provider['id'])
#
#        # Se obtienen los datos de las materias primas para poder eliminarlas
#        raw_materials_json: dict = controller.get('CatalogoMateriasPrimas')
#        for raw_material in raw_materials_json:
#            TestManufactureRawMaterialsController.raw_materials.append(raw_material['id'])
#
#        # Se obtienen los datos de los rubros de materias primas para poder eliminarlos
#        raw_material_categories_json: dict = controller.get('RubrosMateriasPrimas')
#        for category in raw_material_categories_json:
#            TestManufactureRawMaterialsController.raw_material_categories.append(category['id'])

       ##########################################################################################################################
        print(f'Elaboraciones hechas:')
        for elaboration in TestManufactureRawMaterialsController.elaborations:
            print(f'ID: {elaboration.id_raw_material}, Sucursal: {elaboration.id_branch}')
        
        print(f'Compras hechas: {TestManufactureRawMaterialsController.purchases}')
        print(f'Sucursales creadas: {TestManufactureRawMaterialsController.branches}')
        print(f'Localidades creadas: {TestManufactureRawMaterialsController.localities}')
        print(f'Socios creados: {TestManufactureRawMaterialsController.partners}')
        print(f'Proveedores creados: {TestManufactureRawMaterialsController.providers}')
        print(f'Materias primas creadas: {TestManufactureRawMaterialsController.raw_materials}')
        print(f'Rubros de materias primas creados: {TestManufactureRawMaterialsController.raw_material_categories}')
        print()

        for elaboration in TestManufactureRawMaterialsController.elaborations:
            try:
                materia_prima_elaborada_deshecha = controller.delete(f'ElaboracionMateriasPrimas/deshacer')
                print(f'Elaboración deshecha exitosamente de la materia prima {materia_prima_elaborada_deshecha['item1']} en la sucursal {materia_prima_elaborada_deshecha['item2']}')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                self.fail(f"El test falló debido a una excepción: {e}")

        for purchase_id in TestManufactureRawMaterialsController.purchases:
            try:
                controller.post(f'Compras/dar-de-baja/{purchase_id}', {})
                controller.delete(f'Compras/{purchase_id}')
                print(f'Compra {purchase_id} eliminada exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                self.fail(f"El test falló debido a una excepción: {e}")

        for branch_id in TestManufactureRawMaterialsController.branches:
            try:
                controller.delete(f'CatalogoSucursales/{branch_id}')
                print(f'Sucursal {branch_id} eliminada exitosamente')
            except Exception as e:
                self.fail(f"El test falló debido a una excepción: {e}")
        
        for locality_id in TestManufactureRawMaterialsController.localities:
            try:
                controller.delete(f'Localidades/{locality_id}')
                print(f'Localidad {locality_id} eliminada exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                self.fail(f"El test falló debido a una excepción: {e}")

        for partner_id in TestManufactureRawMaterialsController.partners:
            try:
                controller.delete(f'Socios/{partner_id}')
                print(f'Socio {partner_id} eliminado exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                self.fail(f"El test falló debido a una excepción: {e}")

        for provider_id in TestManufactureRawMaterialsController.providers:
            try:
                controller.delete(f'CatalogoProveedores/{provider_id}')
                print(f'Proveedor {provider_id} eliminado exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                self.fail(f"El test falló debido a una excepción: {e}")

        for raw_material_id in TestManufactureRawMaterialsController.raw_materials:
            try:
                controller.delete(f'CatalogoMateriasPrimas/{raw_material_id}')
                print(f'Materia prima {raw_material_id} eliminada exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                self.fail(f"El test falló debido a una excepción: {e}")

        for category_id in TestManufactureRawMaterialsController.raw_material_categories:
            try:
                controller.delete(f'RubrosMateriasPrimas/{category_id}')
                print(f'Rubro de materia prima {category_id} eliminado exitosamente')
            except Exception as e:
                winsound.Beep(FRECUENCY, DURATION)
                self.fail(f"El test falló debido a una excepción: {e}")

        winsound.Beep(FRECUENCY // 3, DURATION // 2)