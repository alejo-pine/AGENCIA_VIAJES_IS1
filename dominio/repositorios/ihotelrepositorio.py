from abc import ABC, abstractmethod
from typing import List
from dominio.entidades.hotel import Hotel

class IHotelRepository(ABC):
    @abstractmethod
    def guardar(self, hotel: Hotel) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id: str) -> Hotel:
        pass

    @abstractmethod
    def listar_hoteles(self) -> List[Hotel]:
        pass

    @abstractmethod
    def eliminar(self, id: str) -> None:
        pass