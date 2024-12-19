from abc import ABC, abstractmethod
from typing import List
from dominio.entidades.excursion import Excursion

class IExcursionRepository(ABC):
    @abstractmethod
    def guardar(self, excursion: Excursion) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id: str) -> Excursion:
        pass

    @abstractmethod
    def listar_excursiones(self) -> List[Excursion]:
        pass

    @abstractmethod
    def eliminar(self, id: str) -> None:
        pass