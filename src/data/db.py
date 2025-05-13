from src.helpers.file_helpers import read_json_file, write_json_file
from src.config.constants import TURNOS_JSON_FILE


def initialize_data() -> list[dict]:
    return read_json_file(TURNOS_JSON_FILE)
