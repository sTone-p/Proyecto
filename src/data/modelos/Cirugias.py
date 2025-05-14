from .Hospital_model import Hospital

class Cirugías(Hospital):
    def __init__(self, nombre: str, edad: int, consulta: str, neurocirugia: str, cirugia_general: str, cirugia_cardiovascular: str):
        super().__init__(nombre, edad, consulta)
        self._neurocirugia: str = neurocirugia
        self._cirugia_general: str = cirugia_general
        self._cirugia_cardiovascular: str = cirugia_cardiovascular


    @property
    def neurocirugia(self) -> str:
        return self._neurocirugia
        
    @neurocirugia.setter
    def neurocirugia(self, neurocirugia: str) -> None:
        self._neurocirugia = neurocirugia

    
    @property
    def cirugia_general(self) -> str:
        return self._cirugia_general
        
    @cirugia_general.setter
    def cirugia_general(self, cirugia_general: str) -> None:
        self._cirugia_general = cirugia_general


    @property
    def cirugia_cardiovascular(self) -> str:
        return self._cirugia_cardiovascular
        
    @cirugia_cardiovascular.setter
    def cirugia_cardiovascular(self, cirugia_cardiovascular: str) -> None:
        self._cirugia_cardiovascular = cirugia_cardiovascular    