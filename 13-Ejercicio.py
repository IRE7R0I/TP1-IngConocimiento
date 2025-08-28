'''
Registro de estudiantes con diccionarios:
Consigna: Una escuela lleva un registro de estudiantes donde la clave es el número de matrícula y el valor es un diccionario con nombre, edad y calificaciones en distintas materias. 
Escribe una función que reciba el registro de estudiantes y devuelva el promedio de calificaciones de un estudiante dado su número de matrícula.
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}
'''
from module.new_functions import is_empty, avg

def avg_califications(dict_students: dict):
    if is_empty(dict_students):
        return {}

    avg_students = []

    for _, data in dict_students.items():
        calificaciones = data['calificaciones'].values()
        promedio = avg(calificaciones)
        avg_students.append((data['nombre'], promedio))

    return avg_students


students = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

print(avg_califications(students))
