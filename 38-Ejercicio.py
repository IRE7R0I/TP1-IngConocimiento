'''
Consigna: Escribe una función que gestione las suscripciones a un servicio en línea.
La función debe recibir el nombre del usuario, el tipo de suscripción (mensual, anual), y cualquier otra opción adicional usando **kwargs. 
La función debe actualizar un diccionario que almacene el historial de suscripciones de los usuarios y devolver el estado actualizado.
suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}
actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)
'''

def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    global suscripciones

    if usuario in suscripciones:
        if suscripcion not in suscripciones[usuario]:
            suscripciones[usuario].append(suscripcion)
    else:
        
        suscripciones[usuario] = [suscripcion]

    if kwargs:
        print(f"Opciones adicionales para {usuario}: {kwargs}")

    return suscripciones

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

actualizado = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print(actualizado)
