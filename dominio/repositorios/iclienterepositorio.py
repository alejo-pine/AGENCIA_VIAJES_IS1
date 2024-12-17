from abc import ABC, abstractmethod
from typing import List

from dominio.entidades.cliente import Cliente


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
    
    @abstractmethod
    def eliminar(self, id: str) -> None:
        pass
