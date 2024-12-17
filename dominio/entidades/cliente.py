from datetime import datetime
from typing import List

from dominio.entidades.historialviaje import HistorialViaje
from dominio.entidades.paqueteturistico import PaqueteTuristico


class Cliente:
    def __init__(self, id: str, nombre: str, direccion: str, correo: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono
        self.historial_viajes: List[HistorialViaje] = []

    def agregar_paquete(self, paquete: PaqueteTuristico) -> None:
        historial = HistorialViaje(
            id=str(len(self.historial_viajes) + 1),
            fecha_viaje=datetime.now(),
            estado="Reservado",
            paquete=paquete
        )
        self.historial_viajes.append(historial)

    def obtener_paquetes(self) -> List[PaqueteTuristico]:
        return [historial.paquete for historial in self.historial_viajes]

    def __repr__(self):
        return f"Cliente({self.id}, {self.nombre}, {self.correo})"