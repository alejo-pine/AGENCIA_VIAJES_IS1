from typing import List
from dominio.entidades.historialviaje import HistorialViaje
from dominio.entidades.cliente import Cliente
from dominio.entidades.paqueteturistico import PaqueteTuristico


class ClienteService:
    @staticmethod
    def validar_cliente(cliente: Cliente) -> None:
        """
        Valida que el cliente tenga todos los datos requeridos.
        """
        if not cliente.nombre:
            raise ValueError("El nombre del cliente es requerido.")
        if not cliente.direccion:
            raise ValueError("La dirección del cliente es requerida.")
        if not cliente.correo or "@" not in cliente.correo:
            raise ValueError("El correo del cliente no es válido.")
        if not cliente.telefono or len(cliente.telefono) < 7:
            raise ValueError("El teléfono del cliente no es válido.")
    
    
    
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