'''
Consigna: Escribe una función que gestione el inventario de una cadena de tiendas. 
La función debe recibir el nombre de la tienda, el producto y la cantidad a actualizar usando **kwargs.
Debe manejar un diccionario donde la clave es el nombre de la tienda y el valor es otro diccionario con los productos y sus cantidades.
La función debe actualizar el inventario y devolver el estado actual.
inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}
actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5)
'''

store_inventory = {
    "Store_A": {"product_1": 50, "product_2": 30},
    "Store_B": {"product_1": 20, "product_2": 40}
}

def update_inventory(store_name, **updated_products):
    if store_name not in store_inventory:
        print(f"Store '{store_name}' not found in inventory.")
        return store_inventory

    for product_name, quantity_change in updated_products.items():
        if product_name in store_inventory[store_name]:
            store_inventory[store_name][product_name] += quantity_change
        else:
            store_inventory[store_name][product_name] = quantity_change

    return store_inventory
