from typing import List
from domain.entidades.historialviaje import HistorialViaje
from domain.entidades.cliente import Cliente
from domain.entidades.paqueteturistico import PaqueteTuristico


class ClienteService:
    @staticmethod
    def registrar_historial_viaje(cliente: Cliente, paquete: PaqueteTuristico) -> None:
        """
        Registra un nuevo historial de viaje para el cliente con un paquete turístico.
        """
        cliente.agregar_paquete(paquete)

    @staticmethod
    def obtener_historial_viajes(cliente: Cliente) -> List[HistorialViaje]:
        """
        Devuelve el historial completo de viajes del cliente.
        """
        return cliente.historial_viajes