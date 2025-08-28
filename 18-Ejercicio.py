'''
Procesamiento de ventas con arrays:Consigna: Una tienda quiere procesar sus ventas diarias almacenadas en un array.
Escribe una función que reciba el array de ventas diarias y devuelva el total de ventas y el promedio de ventas por día.
ventas_diarias = [200, 450, 300, 400, 350, 500, 600]
'''

from module.new_functions import avg

def daily_sales(sales: list):
    print(sum(sales))
    print(avg(sales))


sales = [200, 450, 300, 400, 350, 500, 600]
daily_sales(sales)