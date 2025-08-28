'''
Planificación de viajes con tuplas y diccionarios:
Consigna:
Una agencia de viajes tiene diferentes paquetes turísticos, cada uno representado como una tupla (destino, precio, duración en días). 
Escribe una función que reciba una lista de estos paquetes y devuelva un diccionario con los destinos como claves y el precio total (precio por día * duración) como valor.
paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]
'''

def full_package_price(packeges_list: list):
    for i, items in enumerate(packeges_list):
        print({f'{items[0]}': items[1] * items[2]})


paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

full_package_price(paquetes)