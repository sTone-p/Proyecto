from typing import List

from .db import initialize_data
from .modelos.turno_model import TurnoModel


turnos_db: List[TurnoModel] = initialize_data()