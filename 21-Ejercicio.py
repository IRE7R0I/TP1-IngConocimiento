'''
Ordenamiento de datos con tuplas:
Consigna:
 Escribe una función que reciba una lista de tuplas donde cada tupla contiene un nombre y una puntuación. 
 La función debe devolver la lista ordenada por puntuación de mayor a menor.
 puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
'''

def sorted_points(point_list: list):
    return sorted(point_list, key=lambda x: x[1])


print(sorted_points([("Ana", 85), ("Luis", 90), ("María", 78)]))