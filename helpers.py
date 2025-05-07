import os
from termcolor import colored, cprint


def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')


def menu_turnos():
    cprint('====== HOSPITAL STONE ======', 'green', attrs=['bold', 'blink'])
    cprint('====== T U R N O S ======', 'blue', attrs=['bold', 'blink'])
    cprint('1. Añadir Turno/s.', 'yellow')
    cprint('2. Ver turno/s', 'yellow')
    cprint('3. Editar turno/s', 'yellow')
    cprint('4. Info del paciente', 'yellow')
    cprint('5. Cancelar turno/s', 'yellow')
    print()
    cprint('0. Salir', 'red', attrs=['bold'])