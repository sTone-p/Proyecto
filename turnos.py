# Definición de funciones
from typing import Optional
from data import turnos_db
from constantes import TURNO_DADO, TURNO_DISPONIBLE



def añadir_turno():
    nombre = input('Nombre del Paciente: ')
    while True:
        edad = input('Edad del paciente: ')
        if edad.isnumeric():
            edad = int(edad)
            break
        print("Por favor, ingresa una edad válida (número entero).")
    while True:
        dni = input('D.N.I (Sin puntos ni letras): ')
        if dni.isnumeric():
            break
        print("Por favor, ingresa un D.N.I válido (solo números).")
    obra_social = input('¿Obra Social? S/N: ')
    consulta = input('Razón de la consulta: ')
    turno = {
        'nombre': nombre,
        'edad': edad,
        'dni': dni,
        'obra_social': obra_social,
        'consulta': consulta,
        'dado': False,
    }
    turnos_db.append(turno)
    print('Turno añadido exitosamente')


def ver_turno():
    if not __check_if_turnos():
        return
    for index, turno in enumerate(turnos_db, start=1):
        estado_del_turno = TURNO_DADO if turno['dado'] else TURNO_DISPONIBLE
        print(f"{index}.{turno['nombre']} - {estado_del_turno}")

def editar_turno():
    if not turnos_db:
        print('No hay turnos dados.')
        return
    turno = __find_turno()
    if turno is None:
        return
    new_nombre = input(f'Nuevo Nombre [{turno["nombre"]}]: ')
    new_edad = input(f'Nueva Edad [{turno["edad"]}]: ')
    new_dni = input(f'Nuevo DNI [{turno["dni"]}]: ')
    new_obra_social = input(f'Nueva Obra Social [{turno["obra_social"]}]: ')
    new_consulta = input(f'Nueva consulta [{turno["consulta"]}]: ')
    dado = input(f'Nuevo Turno [{turno["dado"]}]: ')
    if new_nombre:
        turno['nombre'] = new_nombre
    if new_edad.isdigit():
        turno['edad'] = int(new_edad)
    if new_dni:
        turno['dni'] = new_dni
    if new_obra_social:
        turno['obra_social'] = new_obra_social
    if new_consulta:
        turno['consulta'] = new_consulta
    if dado.lower() in ['true', '1', 'sí', 'si']:
        turno['dado'] = True
    elif dado.lower() in ['false', '0', 'no']:
        turno['dado'] = False

    print("✅ Turno editado correctamente.")

def info_de_turno():
    if not turnos_db:
        print('No hay turnos dados.')
        return
    turno = __find_turno()
    if turno is None:
        return
    print(turno)

def cancelar_turno():
    if not __check_if_turnos():
        return 
    ver_turno()
    option = int(input(f'Elije un Turno para cancelar [1-{len(turnos_db)}]'))
    turnos_db.pop(option - 1)
    print('Turno eliminado.')

def __check_if_turnos():
    if not turnos_db:
        print('No hay turnos dados.')
        return False
    return True

def __find_turno() -> Optional[dict]:
    ver_turno()
    option = int(input(f'Elije un Turno [1-{len(turnos_db)}]'))
    for index, turno in enumerate(turnos_db, start=1):
        if option == index:
            return turno
    print('No se encontró el turno.')