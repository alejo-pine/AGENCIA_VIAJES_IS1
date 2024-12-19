
from dominio.entidades.vuelo import Vuelo
from datetime import datetime


class VueloService:
    
    @staticmethod
    def validar_vuelo(vuelo: Vuelo) -> None:
        """
        Valida un vuelo verificando que la fecha sea futura y la disponibilidad de asientos sea positiva.
        """
        if vuelo.fecha < datetime.now():
            raise ValueError("La fecha del vuelo debe ser futura.")
        if vuelo.disponibilidad_asientos <= 0:
            raise ValueError("La disponibilidad de asientos debe ser mayor a 0.")
    