

class Hospital():
    def __init__(self, nombre: str, edad: int, consulta: str):
        self._nombre = nombre
        self._edad = edad
        self._consulta = consulta

    @property
    def nombre(self) -> str:
        return self._nombre
        
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
    

    @property
    def edad(self) -> str:
        return self._edad
        
    @edad.setter
    def edad(self, edad: str) -> None:
        self._edad = edad
    

    @property
    def consulta(self) -> str:
        return self._consulta
        
    @consulta.setter
    def consulta(self, consulta: str) -> None:
        self._consulta = consulta