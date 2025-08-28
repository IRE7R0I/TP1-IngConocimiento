'''
Consigna: Una empresa de logística necesita optimizar sus rutas de entrega.
Cada ruta se representa como una tupla (origen, destino, distancia). 
Escribe una función que reciba una lista de rutas y un array con las distancias máximas permitidas para cada ruta. 
La función debe devolver las rutas que cumplen con las restricciones.
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]
'''

def condition_rutes(rutes, condition):

    condition_completed = list()

    for rute, max_dist in zip(rutes, condition):
        if rute[2] <= max_dist:
            condition_completed.append(rute)
    
    return condition_completed

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

condition_completed_rutes = condition_rutes(rutas, distancias_max)

print(condition_completed_rutes)