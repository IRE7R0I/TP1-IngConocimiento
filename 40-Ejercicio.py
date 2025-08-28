'''
Consigna: 
Una universidad lleva un registro de las calificaciones de los estudiantes en diferentes materias. 
Cada estudiante tiene un ID único y su información se almacena en un diccionario donde la clave es el ID y el valor es otro diccionario con las materias y sus respectivas calificaciones (arrays). 
Escribe una función que reciba este diccionario y devuelva un ranking de estudiantes basado en su promedio general.
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
'''

from module.new_functions import avg

def ranking_students( students_dict):
    ranking = list()

    for key, value in students_dict.items():
        average = round(avg(sum(value["matemáticas"]) + sum(value["ciencias"]), count= 3))
        ranking.append([key, average])
    
    ranking.sort(key = lambda x: x[1], reverse=True)

    print(ranking)

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking_students(estudiantes)