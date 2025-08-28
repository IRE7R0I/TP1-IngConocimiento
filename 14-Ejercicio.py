'''
Análisis de datos meteorológicos con arrays:
Consigna: Un meteorólogo registra las temperaturas diarias durante un mes y las almacena en un array. 
Escribe una función que reciba este array y devuelva la temperatura media del mes, la máxima y la mínima.
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
'''

from module.new_functions import avg

max_temperature = lambda temperature: [] if not temperature else max(temperature)
min_temperature = lambda temperature: [] if not temperature else min(temperature)
avg_temperature = lambda temperature: [] if not temperature else round(avg(temperature))



temerature = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
print(max_temperature(temerature))
print(min_temperature(temerature))
print(avg_temperature(temerature))