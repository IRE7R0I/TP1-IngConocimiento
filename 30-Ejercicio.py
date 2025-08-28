'''
Configuración de perfiles de usuario con **kwargs y arrays:
Consigna: Escribe una función que reciba una lista de usuarios y sus preferencias de configuración como **kwargs. 
La función debe devolver un diccionario donde la clave es el nombre del usuario y el valor es un array con las configuraciones aplicadas.
usuarios = ["Ana", "Luis", "María"]
configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
}
'''
def configurate_profile(names: list, **configurations):
    profile_dict = dict()

    for _, name in enumerate(names):
        profile_dict[name] = configurations

    return profile_dict

usuarios = ["Ana", "Luis", "María"]

print(configurate_profile(usuarios, idioma="es", modo_oscuro=True, notificaciones=False))