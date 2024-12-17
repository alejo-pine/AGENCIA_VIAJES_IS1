from abc import ABC, abstractmethod
from typing import List

from domain.entidades.cliente import Cliente


class IClienteRepository(ABC):
    @abstractmethod
    def guardar(self, cliente: Cliente) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id: str) -> Cliente:
        pass

    @abstractmethod
    def listar_clientes(self) -> List[Cliente]:
        pass
