from datetime import datetime

from domain.entidades.proveedor import Proveedor


class Vuelo:
    def __init__(self, id: str, aerolinea: str, destino: str, fecha: datetime, disponibilidad_asientos: int, precio: float, proveedor: Proveedor):
        self.id = id
        self.aerolinea = aerolinea
        self.destino = destino
        self.fecha = fecha
        self.disponibilidad_asientos = disponibilidad_asientos
        self.precio = precio
        self.proveedor = proveedor

    def verificar_disponibilidad(self) -> bool:
        return self.disponibilidad_asientos > 0

    def actualizar_disponibilidad(self, cantidad: int) -> None:
        self.disponibilidad_asientos -= cantidad

    def __repr__(self):
        return f"Vuelo({self.aerolinea}, {self.destino}, Disponibles: {self.disponibilidad_asientos})"
