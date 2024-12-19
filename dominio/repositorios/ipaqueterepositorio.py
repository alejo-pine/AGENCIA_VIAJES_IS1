from abc import ABC, abstractmethod
from typing import List

from dominio.entidades.paqueteturistico import PaqueteTuristico


class IPaqueteRepository(ABC):
    @abstractmethod
    def guardar(self, paquete: PaqueteTuristico) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id: str) -> PaqueteTuristico:
        pass

    @abstractmethod
    def listar_paquetes(self) -> List[PaqueteTuristico]:
        pass
    
    @abstractmethod
    def eliminar(self, id: str) -> None:
        pass