'''
Consigna: 
Una empresa de marketing digital desea analizar las tendencias de hashtags en las redes sociales. 
Escribe una función que reciba un array de hashtags y una lista de tuplas donde cada tupla contiene un hashtag y su frecuencia de uso. 
La función debe devolver los hashtags que han sido mencionados más de una cierta cantidad de veces.
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"] tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]
'''

def filtrar_hashtags(hashtags, tendencias, umbral):
    hashtags_validos = []

    
    frecuencia_dict = dict(tendencias)

    
    for hashtag in set(hashtags):
        if frecuencia_dict.get(hashtag, 0) > umbral:
            hashtags_validos.append(hashtag)

    return hashtags_validos

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

resultado = filtrar_hashtags(hashtags, tendencias, umbral=100)
print(resultado)

