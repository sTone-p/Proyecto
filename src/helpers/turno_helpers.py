from termcolor import cprint
from src.config.constants import TURNO_DADO, TURNO_DISPONIBLE, TURNOS_JSON_FILE
from src.helpers.file_helpers import write_json_file
from src.data import turnos_db


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


def save_turnos() -> None:
    write_json_file(TURNOS_JSON_FILE, turnos_db)

