'''
Análisis de resultados deportivos con diccionarios:
Consigna: Un club deportivo registra los resultados de sus partidos en un diccionario donde la clave es el nombre del equipo rival y el valor es una tupla con los goles anotados y recibidos. 
Escribe una función que calcule el total de goles anotados y recibidos en la temporada.
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}
'''

def season_results(results: dict):
    counter_goals, counter_goals_received = 0, 0

    for key, _ in results.items():
        counter_goals += results[key][0]
        counter_goals_received += results[key][1]
    
    print(f'Goles marcados: {counter_goals}')
    print(f'Goles recibidos: {counter_goals_received}')


resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

season_results(resultados)