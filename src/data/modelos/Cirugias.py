from .Hospital_model import Hospital

class Cirugías(Hospital):
    def __init__(self, nombre: str, edad: int, consulta: str, neurocirugia: str, cirugia_general: str, cirugia_cardiovascular: str, medico_neuro: str, medico_general: str, medico_cardio: str):
        super().__init__(nombre, edad, consulta)
        self._neurocirugia: str = neurocirugia
        self._cirugia_general: str = cirugia_general
        self._cirugia_cardiovascular: str = cirugia_cardiovascular
        self._medico_neuro = medico_neuro
        self._medico_general = medico_general
        self._medico_cardio = medico_cardio


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


    @property
    def medico_neuro(self) -> str:
        return self._medico_neuro

    @medico_neuro.setter
    def medico_neuro(self, nombre: str) -> None:
        if not nombre:
            raise ValueError("El nombre del médico de neurocirugía no puede estar vacío.")
        self._medico_neuro = nombre


    @property
    def medico_general(self) -> str:
        return self._medico_general

    @medico_general.setter
    def medico_general(self, nombre: str) -> None:
        if not nombre:
            raise ValueError("El nombre del médico de cirugía general no puede estar vacío.")
        self._medico_general = nombre


    @property
    def medico_cardio(self) -> str:
        return self._medico_cardio

    @medico_cardio.setter
    def medico_cardio(self, nombre: str) -> None:
        if not nombre:
            raise ValueError("El nombre del médico de cirugía cardiovascular no puede estar vacío.")
        self._medico_cardio = nombre
    

    def mostrar_resumen(self) -> str:
        return (
        f"Paciente: {self.nombre} | Edad: {self.edad}\n"
        f"Consulta: {self.consulta}\n"
        f"Neurocirugía: {self.neurocirugia} (Dr. {self.medico_neuro})\n"
        f"Cirugía General: {self.cirugia_general} (Dr. {self.medico_general})\n"
        f"Cirugía Cardiovascular: {self.cirugia_cardiovascular} (Dr. {self.medico_cardio})"
    )