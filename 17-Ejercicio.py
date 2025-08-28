'''
Administración de empleados con tuplas y diccionarios:Consigna: Una empresa quiere administrar la información de sus empleados, donde cada empleado se representa como una tupla (nombre, edad, salario).
 Escribe una función que reciba un diccionario donde la clave es el ID del empleado y el valor es la tupla con su información. 
 La función debe devolver un diccionario con los empleados que ganan más de un salario dado.
empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}
'''

def given_salary(employees_dict: dict, salary_min: float):
    for key, _ in employees_dict.items():
        if employees_dict[key][2] >= salary_min:
            print(employees_dict[key])



employees = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

given_salary(employees, 3000)
