from typing import List

from .db import initialize_data
from .modelos.turno_model import Cirugía


turnos_db: List[Cirugía] = initialize_data()