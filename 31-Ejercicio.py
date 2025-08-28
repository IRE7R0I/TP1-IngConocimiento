'''
Consigna: 
Escribe una función que administre publicaciones de una red social.
La función debe recibir el nombre del usuario, el texto de la publicación y un número variable de etiquetas usando **kwargs y arrays. 
Además, debe manejar opciones adicionales como visibilidad pública o privada. 
La función debe devolver un diccionario con todos los detalles de la publicación.
publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)
'''

def publicate(name:str, description:str, **publication_atributes):
    publication = {'nombre': name, 'descripcion': description}
    publication.update(publication_atributes)

    print(publication)

publicate("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)

    