'''
Manejo de parámetros variables con *args:Consigna: Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota promedio. 
Utiliza *args para recibir las notas.calcular_promedio(85, 90, 78, 92)
'''

from module.new_functions import avg

def calculate_avg(*args):
    total = sum(args)
    print(avg(total, count = len(args)))



print(calculate_avg(85, 90, 78, 92))
    