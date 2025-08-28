'''
Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un estudiante y sus calificaciones en un array. 
La función debe devolver un diccionario con el nombre del estudiante como clave y su promedio de calificaciones como valor.
notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

'''
from module.new_functions import avg

def marks(marks_students: list):
    marks_dict = dict()

    for i, value in enumerate(marks_students):
        marks_dict[value[0]] = round(avg(value[1]))
    
    return marks_dict


notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

print(marks(notas_estudiantes))