from dominio.entidades.paqueteturistico import PaqueteTuristico


class PaqueteService:
    @staticmethod
    def calcular_precio_paquete(paquete: PaqueteTuristico) -> float:
        """
        Calcula el precio total de un paquete turístico sumando los precios de vuelos, hoteles y excursiones.
        """
        return paquete.calcular_precio()

    @staticmethod
    def verificar_disponibilidad_paquete(paquete: PaqueteTuristico) -> bool:
        """
        Verifica si todos los componentes del paquete turístico tienen disponibilidad.
        """
        return paquete.verificar_disponibilidad()

    @staticmethod
    def ajustar_precio_por_demanda(paquete: PaqueteTuristico, demanda: float) -> None:
        """
        Ajusta el precio del paquete turístico en función de la demanda.
        """
        paquete.ajustar_precio_demanda(demanda)