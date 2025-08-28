'''
Consigna: 
Escribe una función que reciba el nombre, edad, y salario de un empleado como parámetros obligatorios, y otros datos como dirección, número de teléfono, etc., como **kwargs.
La función debe devolver un diccionario con toda la información del empleado.
registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")
'''

def register_employee(name, age, salary, **employee_properties):
    employee = {'nombre': name, 'edad': age, 'salario': salary}
    employee.update(employee_properties)

    return employee

print(register_employee("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789"))