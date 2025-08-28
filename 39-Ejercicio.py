'''
Consigna: Escribe una función que simule el comportamiento de acciones en un mercado bursátil. 
La función debe recibir un array con los precios diarios de una acción y una lista de tuplas donde cada tupla contiene un día y un precio de compra o venta. 
La función debe devolver el beneficio o pérdida total si las acciones se hubieran comprado y vendido en los días especificados.
precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]
'''

def calcular_beneficio(precios_diarios, operaciones):
    beneficio_total = 0
    acciones_en_cartera = []

    for operacion, dia in operaciones:
        precio = precios_diarios[dia]

        if operacion == "compra":
            acciones_en_cartera.append(precio)
        elif operacion == "venta":
            if acciones_en_cartera:
                precio_compra = acciones_en_cartera.pop(0)
                beneficio = precio - precio_compra
                beneficio_total += beneficio
            else:
                print(f"⚠️ No hay acciones para vender en el día {dia}")

    return beneficio_total


precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

resultado = calcular_beneficio(precios_diarios, operaciones)
print(f"Beneficio total: ${resultado}")
