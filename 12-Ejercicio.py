'''
Gestión de inventario con tuplas:
Consigna: Una tienda tiene un inventario de productos, cada producto tiene un nombre, precio y cantidad disponible. 
Representa cada producto como una tupla (nombre, precio, cantidad). 
Escribe una función que reciba una lista de productos (tuplas) y devuelva el producto más caro.
productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]
'''
from module.new_functions import is_empty

def most_expensive_product(products: list):
    if is_empty(products):
        return []

    return max(products, key= lambda product: product[1])


products = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

print(most_expensive_product(products))