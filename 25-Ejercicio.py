'''
Análisis financiero con **kwargs:
Consigna: Escribe una función que reciba diferentes tipos de ingresos y gastos como **kwargs y calcule el balance final. 
La función debe manejar ingresos como positivos y gastos como negativos.
analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
'''
def analyze_finances(**finances):
    sum_positive, sum_negative = 0, 0

    for _, value in finances.items():
        if value < 0:
            sum_negative += value
        elif value > 0:
            sum_positive += value
    
    print(sum_negative, sum_positive, sum_positive + sum_negative)

analyze_finances(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)