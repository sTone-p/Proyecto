#RUN DEFINICIÓN

from termcolor import cprint, colored

from src.controllers import turnos
from src.helpers.consola_helper import limpiar_consola, menu_turnos
from src.helpers import consola_helper

def run():
    limpiar_consola
    while True:
        menu_turnos()
        option = input(colored('Elija una Opción [0-5]: ', 'cyan'))
        limpiar_consola()
        match option:
            case '1':
                turnos.añadir_turno()
            case '2':
                turnos.ver_turno()
            case '3':
                turnos.editar_turno()
            case '4':
                turnos.info_de_turno()
            case '5':
                turnos.cancelar_turno()
            case '0': 
                cprint('Saliendo...', 'red', attrs=['bold'])
                break
            case _:
                cprint('Opción Inválida.', 'red', attrs=['bold'])