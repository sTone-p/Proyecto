from typing import List

from src.helpers.file_helpers import read_json_file, write_json_file
from src.config.constants import TURNOS_JSON_FILE
from .modelos.turno_model import Cirugía

def initialize_data() -> List[Cirugía]:
    lista_turnos: list[dict] = read_json_file(TURNOS_JSON_FILE)
    return [Cirugía(**turno_dict) for turno_dict in lista_turnos]