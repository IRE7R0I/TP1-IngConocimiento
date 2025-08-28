'''
Consigna: Una empresa realiza encuestas de satisfacción y registra las respuestas en un diccionario donde la clave es la pregunta y el valor es un array con las respuestas recibidas. 
Escribe una función que calcule la frecuencia de cada respuesta para cada pregunta y devuelva un diccionario con estos resultados.
encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}
'''

def calcular_frecuencias(encuestas):
    resultados = {}

    for pregunta, respuestas in encuestas.items():
        frecuencias = {}
        for respuesta in respuestas:
            if respuesta in frecuencias:
                frecuencias[respuesta] += 1
            else:
                frecuencias[respuesta] = 1
        resultados[pregunta] = frecuencias

    return resultados

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

frecuencias = calcular_frecuencias(encuestas)
print(frecuencias)

            