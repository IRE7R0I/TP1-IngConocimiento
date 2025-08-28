'''
Consigna: Una tienda maneja su inventario de productos en un array donde cada índice representa un producto específico y su valor es la cantidad disponible.
Escribe una función que reciba el array de inventario y un número de productos vendidos (otro array) y devuelva el inventario actualizado.
inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]
'''

def update_inventory(inv_list, sales_list):
    for i, _ in enumerate(inv_list):
        inv_list[i] -= sales_list[i]
    
    return inv_list

print(update_inventory([50, 30, 20, 10], [5, 10, 5, 2]))