from abc import ABC, abstractmethod
from typing import List

from dominio.entidades.proveedor import Proveedor


class IProveedorRepository(ABC):
    @abstractmethod
    def guardar(self, proveedor: Proveedor) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id: str) -> Proveedor:
        pass

    @abstractmethod
    def listar_proveedores(self) -> List[Proveedor]:
        pass