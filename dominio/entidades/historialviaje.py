from datetime import datetime

from dominio.entidades.paqueteturistico import PaqueteTuristico


class HistorialViaje:
    def __init__(self, id: str, fecha_viaje: datetime, estado: str, paquete: PaqueteTuristico):
        self.id = id
        self.fecha_viaje = fecha_viaje
        self.estado = estado
        self.paquete = paquete

    def __repr__(self):
        return f"HistorialViaje({self.id}, {self.fecha_viaje}, {self.estado})"