from abc import ABC, abstractmethod
from typing import List
from dominio.entidades.vuelo import Vuelo

class IVueloRepository(ABC):
    @abstractmethod
    def guardar(self, vuelo: Vuelo) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id: str) -> Vuelo:
        pass

    @abstractmethod
    def listar_vuelos(self) -> List[Vuelo]:
        pass

    @abstractmethod
    def eliminar(self, id: str) -> None:
        pass