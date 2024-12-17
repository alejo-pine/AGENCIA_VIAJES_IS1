from abc import ABC, abstractmethod
from typing import List

from domain.entidades.factura import Factura


class IFacturaRepository(ABC):
    @abstractmethod
    def guardar(self, factura: Factura) -> None:
        pass

    @abstractmethod
    def buscar_por_cliente(self, cliente_id: str) -> List[Factura]:
        pass

    @abstractmethod
    def listar_facturas(self) -> List[Factura]:
        pass