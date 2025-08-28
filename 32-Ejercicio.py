'''
Consigna: Una empresa quiere simular las ventas de diferentes productos. 
Escribe una función que reciba un número variable de ventas (tuplas) donde cada tupla contiene el producto, la cantidad vendida, y el precio por unidad. 
La función debe devolver el total de ingresos generados por las ventas.
simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))
'''

def sales_simulator(*args):
    total_profit = 0

    for product, cuantity, price in args:
        total_profit += (cuantity * price)

    print(total_profit)


sales_simulator(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))
