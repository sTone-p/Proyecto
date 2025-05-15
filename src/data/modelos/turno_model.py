from .Hospital_model import Hospital

class TurnoModel(Hospital):
    def __init__(self, nombre: str, edad: int, dni: str, obra_social: str, consulta: str, dado: bool = False ):
        super().__init__(nombre, edad, consulta)
        self.dni: str = dni
        self.obra_social: str = obra_social
        self.dado: bool = dado
    
    def to_json(self) -> dict:
        return {
            "nombre": self._nombre,
            "edad": self._edad, 
            "consulta": self._consulta,
            "dni": self.dni,
            "obra social": self.obra_social,
            "dado": self.dado

        }
    
    def __str__(self):
        return (
            f"--- Ficha del Paciente ---\n"
            f"Nombre       : {self.nombre}\n"
            f"Edad         : {self.edad}\n"
            f"DNI          : {self.dni}\n"
            f"Obra Social  : {self.obra_social}\n"
            f"Consulta     : {self.consulta}\n"
        )
    
