'''
Estadísticas de ventas con arrays:
Consigna: Escribe una función que reciba un array con las ventas de cada mes y devuelva un diccionario con el total de ventas, el promedio mensual, y el mes con mayores ventas.
ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
'''

from module.new_functions import avg

def mensual_sales(sales: list):
    return f'Total de ventas: {sum(sales)}\nPromedio Mensual: {round(avg(sales))}\nMes con mayores ventas: {sales.index(max(sales)) + 1}'


ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
print(mensual_sales(ventas_mensuales))