from datetime import datetime

from domain.entidades.proveedor import Proveedor


class Excursion:
    def __init__(self, id: str, lugar: str, fecha: datetime, precio: float, disponibilidad_plazas: int, proveedor: Proveedor):
        self.id = id
        self.lugar = lugar
        self.fecha = fecha
        self.precio = precio
        self.disponibilidad_plazas = disponibilidad_plazas
        self.proveedor = proveedor

    def verificar_disponibilidad(self) -> bool:
        return self.disponibilidad_plazas > 0

    def actualizar_disponibilidad(self, cantidad: int) -> None:
        self.disponibilidad_plazas -= cantidad

    def __repr__(self):
        return f"Excursion({self.lugar}, Disponibles: {self.disponibilidad_plazas})"