from abc import ABC, abstractmethod
from typing import List
from dominio.entidades.contrato import Contrato

class IContratoRepository(ABC):
    @abstractmethod
    def guardar(self, contrato: Contrato) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id: str) -> Contrato:
        pass

    @abstractmethod
    def listar_contratos(self) -> List[Contrato]:
        pass

    @abstractmethod
    def eliminar(self, id: str) -> None:
        pass