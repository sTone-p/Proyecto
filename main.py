#IMPORTACION DE RUN
from termcolor import cprint, colored
from helpers import limpiar_consola, menu_turnos
from turnos import añadir_turno, ver_turno, info_de_turno, editar_turno, cancelar_turno

def run():
    limpiar_consola
    while True:
        menu_turnos()
        option = input(colored('Elija una Opción [0-5]: ', 'cyan'))
        limpiar_consola()
        match option:
            case '1':
                añadir_turno()
            case '2':
                ver_turno()
            case '3':
                editar_turno()
            case '4':
                info_de_turno()
            case '5':
                cancelar_turno()
            case '0': 
                cprint('Saliendo...', 'red', attrs=['bold'])
                break
            case _:
                cprint('Opción Inválida.', 'red', attrs=['bold'])

if __name__ == '__main__':
    run()
