from datetime import datetime
from typing import List

from dominio.entidades.contrato import Contrato


class Proveedor:
    def __init__(self, id: str, nombre: str, tipo: str):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.contratos: List[Contrato] = []

    def registrar_contrato(self, contrato: Contrato) -> None:
        self.contratos.append(contrato)

    def alerta_renovacion_contrato(self) -> bool:
        hoy = datetime.now()
        return any((contrato.fecha_expiracion - hoy).days <= 30 for contrato in self.contratos)

    def __repr__(self):
        return f"Proveedor({self.nombre}, Tipo: {self.tipo})"