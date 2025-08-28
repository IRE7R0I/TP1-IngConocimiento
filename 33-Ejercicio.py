'''
Consigna: Un hotel maneja sus reservas utilizando un diccionario donde la clave es la fecha y el valor es una lista de tuplas, cada tupla contiene el nombre del huésped, la habitación asignada y el precio. 
Escribe una función que permita hacer una nueva reserva verificando primero si la habitación está disponible en la fecha seleccionada.
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}
'''



def make_reservation(reservations: dict, date_reservation, name, room, price):
    nueva_reserva = (name, room, price)

   
    if date_reservation in reservations:
        
        for reserva in reservations[date_reservation]:
            if reserva[1] == room:
                print('Ya hay una reservación hecha para esa habitación en esa fecha.')
                return
        
        reservations[date_reservation].append(nueva_reserva)
        print('Reservación realizada.')
        print(reservations)
    else:
        
        reservations[date_reservation] = [nueva_reserva]
        print('Reservación realizada.')
        print(reservations)
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

make_reservation(reservas, '2024-08-15', 'Pepe', 101, 150) 
make_reservation(reservas, '2024-08-15', 'Pepe', 103, 150)  
make_reservation(reservas, '2024-08-17', 'Lucía', 104, 200)