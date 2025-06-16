from typing import Optional
from api.models.Rubro.RawMaterialCategory import RawMaterialCategory
from api.models.Sucursal.Branch import Branch
from api.models.Unidad.Unit import Unit
from api.models.Usuarios.User import User
from datetime import datetime

class RawMaterial:
    def __init__(self, id: int, category: RawMaterialCategory, unit: Unit, name: str, source: str, stock: int, discarded: int, picture: str, comment: Optional[str] = None):
        self.id = id
        self.category = category
        self.unit = unit
        self.name = name
        self.source = source
        self.stock = stock
        self.discarded = discarded
        self.picture = picture
        self.comment = comment

    def to_json(self):
        return {
            'id': self.id,
            'category': self.category.to_json(),
            'unit': self.unit.to_json(),
            'name': self.name,
            'source': self.source,
            'stock': self.stock,
            'discarded': self.discarded,
            'picture': self.picture,
            'comment': self.comment
        }

    @staticmethod
    def json_to_object(json: dict):
        return RawMaterial(
            json['id'],
            RawMaterialCategory.json_to_object(json['category']),
            Unit.json_to_object(json['unit']),
            json['name'],
            json['source'],
            json['stock'],
            json['discarded'],
            json['picture'],
            json['comment']
        )

class StoredRawMaterial(RawMaterial):
    def __init__(self, id: int, category: RawMaterialCategory, unit: Unit, name: str, source: str, stock: int, discarded: int, stock_in_branch: int, discarded_in_branch: int, picture: str, branch: Branch, comment: Optional[str] = None):
        super().__init__(id, category, unit, name, source, stock, discarded, picture, comment)
        self.stock_in_branch = stock_in_branch
        self.discarded_in_branch = discarded_in_branch
        self.branch = branch
    
    def to_json(self):
        return {
            'id': self.id,
            'category': self.category.to_json(),
            'unit': self.unit.to_json(),
            'name': self.name,
            'source': self.source,
            'stock': self.stock,
            'discarded': self.discarded,
            'stock_in_branch': self.stock_in_branch,
            'discarded_in_branch': self.discarded_in_branch,
            'picture': self.picture,
            'branch': self.branch.to_json(),
            'comment': self.comment
        }
    
    @staticmethod
    def json_to_object(json: dict):
        return StoredRawMaterial(
            json['id'],
            RawMaterialCategory.json_to_object(json['category']),
            Unit.json_to_object(json['unit']),
            json['name'],
            json['source'],
            json['stock'],
            json['discarded'],
            json['stock_in_branch'],
            json['discarded_in_branch'],
            json['picture'],
            Branch.json_to_object(json['branch']),
            json['comment']
        )

class ManufacturedRawMaterial:
    def __init__(self, id_entry: int, id_manufacture: int, raw_material: RawMaterial, manufacturing_date: datetime, quantity: int, manufacturer: User, production_branch: Branch, stock_in_branch: int, discarded_in_branch: int, comment: Optional[str] = None):
        self.id_entry = id_entry
        self.id_manufacture = id_manufacture
        self.raw_material = raw_material
        self.manufacturing_date = manufacturing_date
        self.quantity = quantity
        self.manufacturer = manufacturer
        self.production_branch = production_branch
        self.stock_in_branch = stock_in_branch
        self.discarded_in_branch = discarded_in_branch
        self.comment = comment

    def to_json(self):
        return {
            'id_entry': self.id_entry,
            'id_manufacture': self.id_manufacture,
            'raw_material': self.raw_material.to_json(),
            'manufacturing_date': self.manufacturing_date.isoformat(),
            'quantity': self.quantity,
            'manufacturer': self.manufacturer.to_json(),
            'production_branch': self.production_branch.to_json(),
            'stock_in_branch': self.stock_in_branch,
            'discarded_in_branch': self.discarded_in_branch,
            'comment': self.comment
        }

    @staticmethod
    def json_to_object(json: dict):
        return ManufacturedRawMaterial(
            json['id_entry'],
            json['id_manufacture'],
            RawMaterial.json_to_object(json['raw_material']),
            datetime.fromisoformat(json['manufacturing_date']),
            json['quantity'],
            User.json_to_object(json['manufacturer']),
            Branch.json_to_object(json['production_branch']),
            json['stock_in_branch'],
            json['discarded_in_branch'],
            json['comment']
        )

class UsedRawMaterial:
    def __init__(self, id_exit: int, id_manufacture: int, raw_material: RawMaterial, manufacturing_date: datetime, quantity: int, manufacturer: User, production_branch: Branch, stock_in_branch: int, discarded_in_branch: int, comment: Optional[str] = None):
        self.id_exit = id_exit
        self.id_manufacture = id_manufacture
        self.raw_material = raw_material
        self.manufacturing_date = manufacturing_date
        self.quantity = quantity
        self.manufacturer = manufacturer
        self.production_branch = production_branch
        self.stock_in_branch = stock_in_branch
        self.discarded_in_branch = discarded_in_branch
        self.comment = comment

    def to_json(self):
        return {
            'id_exit': self.id_exit,
            'id_manufacture': self.id_manufacture,
            'raw_material': self.raw_material.to_json(),
            'manufacturing_date': self.manufacturing_date.isoformat(),
            'quantity': self.quantity,
            'manufacturer': self.manufacturer.to_json(),
            'production_branch': self.production_branch.to_json(),
            'stock_in_branch': self.stock_in_branch,
            'discarded_in_branch': self.discarded_in_branch,
            'comment': self.comment
        }

    @staticmethod
    def json_to_object(json: dict):
        return UsedRawMaterial(
            json['id_exit'],
            json['id_manufacture'],
            RawMaterial.json_to_object(json['raw_material']),
            datetime.fromisoformat(json['manufacturing_date']),
            json['quantity'],
            User.json_to_object(json['manufacturer']),
            Branch.json_to_object(json['production_branch']),
            json['stock_in_branch'],
            json['discarded_in_branch'],
            json['comment']
        )

class RawMaterialPackage:
    def __init__(self, raw_material: RawMaterial, quantity: int):
        self.raw_material = raw_material
        self.quantity = quantity
    
    def to_json(self):
        return {
            'raw_material': self.raw_material.to_json(),
            'quantity': self.quantity
        }

    @staticmethod
    def json_to_object(json: dict):
        return RawMaterialPackage(
            RawMaterial.json_to_object(json['raw_material']),
            json['quantity']
        )

class ManufacturePackage:
    def __init__(self, elaborated_raw_materials: list[RawMaterialPackage], used_raw_materials: list[RawMaterialPackage], user: User, branch: Branch, manufacturing_date: datetime):
        self.elaborated_raw_materials = elaborated_raw_materials
        self.used_raw_materials = used_raw_materials
        self.user = user
        self.branch = branch
        self.manufacturing_date = manufacturing_date
    
    def to_json(self):
        return {
            'elaborated_raw_materials': [raw_material.to_json() for raw_material in self.elaborated_raw_materials],
            'used_raw_materials': [raw_material.to_json() for raw_material in self.used_raw_materials],
            'user': self.user.to_json(),
            'branch': self.branch.to_json(),
            'manufacturing_date': self.manufacturing_date.isoformat()
        }

    @staticmethod
    def json_to_object(json: dict):
        return ManufacturePackage(
            [RawMaterialPackage.json_to_object(raw_material) for raw_material in json['elaborated_raw_materials']],
            [RawMaterialPackage.json_to_object(raw_material) for raw_material in json['used_raw_materials']],
            User.json_to_object(json['user']),
            Branch.json_to_object(json['branch']),
            datetime.fromisoformat(json['manufacturing_date'])
        )

class ManufactureRawMaterial:
    def __init__(self, id_raw_material: int, stock: int, stock_in_branch: int, qnty_to_use: int):
        self.id_raw_material = id_raw_material
        self.stock = stock
        self.stock_in_branch = stock_in_branch
        self.qnty_to_use = qnty_to_use
    
    def to_json(self):
        return {
            'id_raw_material': self.id_raw_material,
            'stock': self.stock,
            'stock_in_branch': self.stock_in_branch,
            'qnty_to_use': self.qnty_to_use
        }

    @staticmethod
    def json_to_object(json: dict):
        return ManufactureRawMaterial(
            json['id_raw_material'],
            json['stock'],
            json['stock_in_branch'],
            json['qnty_to_use']
        )

class RawMaterialManufacture:
    def __init__(self, idRawMaterial: int, quantity: int, idUser: int, idBranch: int, materialsList: list[ManufactureRawMaterial], comment: Optional[str] = None):
        self.id_raw_material = idRawMaterial
        self.quantity = quantity
        self.idUser = idUser
        self.idBranch = idBranch
        self.materialsList = materialsList
        self.comment = comment

    def to_json(self):
        return {
            'id_raw_material': self.id_raw_material,
            'quantity': self.quantity,
            'idUser': self.idUser,
            'idBranch': self.idBranch,
            'materialsList': [material.to_json() for material in self.materialsList],
            'comment': self.comment
        }
    
    @staticmethod
    def json_to_object(json: dict):
        return RawMaterialManufacture(
            json['id_raw_material'],
            json['quantity'],
            json['idUser'],
            json['idBranch'],
            [ManufactureRawMaterial.json_to_object(material) for material in json['materialsList']],
            json['comment']
        )