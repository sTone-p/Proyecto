

class Cirugía():
    def __init__(self, nombre: str, edad: int, dni: str, obra_social: str, consulta: str, dado: bool = False ):
        self.nombre: str = nombre
        self.edad: int = edad
        self.dni: str = dni
        self.obra_social: str = obra_social
        self.consulta: str = consulta
        self.dado: bool = dado
    
    def to_json(self):
        return self.__dict__
    
