'''
Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
“Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)”
'''


try:
    name_associate = input('Ingrese el nombre del asociado: ')
    num_associate = int(input('Ingrese el numero del asociado: '))

    print(f'Estimado/a {name_associate}, su número de asociado es: {num_associate}')
except ValueError:
    print('Hubo un error a la hora de ingresar el numero del asociado')

    