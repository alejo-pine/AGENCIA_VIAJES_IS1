

from dominio.entidades.hotel import Hotel


class HotelService: 
    
    @staticmethod
    def validar_hotel(hotel: Hotel) -> None:
        """
        Valida un hotel verificando que el precio sea positivo y la disponibilidad de habitaciones sea positiva.
        """
        if hotel.precio <= 0:
            raise ValueError("El precio del hotel debe ser mayor a 0.")
        if hotel.disponibilidad_habitaciones <= 0:
            raise ValueError("La disponibilidad de habitaciones debe ser mayor a 0.")