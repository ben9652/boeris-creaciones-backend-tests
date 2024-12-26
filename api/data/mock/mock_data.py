import random

def generate_addresses():
    # Leer el archivo local `addresses.txt` y retornar un arreglo con las direcciones separadas por un salto de línea
    with open("api/data/mock/addresses.txt") as f:
        return f.read().split("\n")
    
def generate_first_names():
    # Leer el archivo local `first_names.txt` y retornar un arreglo con los nombres separados por un salto de línea
    with open("api/data/mock/first_names.txt") as f:
        return f.read().split("\n")

def generate_last_names():
    # Leer el archivo local `last_names.txt` y retornar un arreglo con los apellidos separados por un salto de línea
    with open("api/data/mock/last_names.txt") as f:
        return f.read().split("\n")
    
def generate_phones():
    # Leer el archivo local `phones.txt` y retornar un arreglo con los teléfonos separados por un salto de línea
    with open("api/data/mock/phones.txt") as f:
        return f.read().split("\n")
    
def generate_raw_material_categories():
    with open("api/data/mock/raw_material_categories.txt") as f:
        return f.read().split("\n")

def generate_raw_material_names():
    with open("api/data/mock/raw_material_names.txt") as f:
        return f.read().split("\n")
    
def generate_purchases_descriptions():
    with open("api/data/mock/purchases_descriptions.txt") as f:
        return f.read().split("\n")
    
def generate_provider_names():
    with open("api/data/mock/provider_names.txt") as f:
        return f.read().split("\n")