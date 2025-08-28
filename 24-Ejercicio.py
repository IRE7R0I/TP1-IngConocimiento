'''
Consigna: Escribe una función que reciba un número variable de nombres de eventos y los imprima en un formato de lista numerada.
 Utiliza *args para recibir los nombres de los eventos.
organizar_eventos("Concierto", "Exposición de arte", "Conferencia")
'''

def organize_events(*events):
    for i, event in enumerate(events):
        print(f'{i + 1}. {event}')

organize_events("Concierto", "Exposición de arte", "Conferencia")