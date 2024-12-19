
from dominio.entidades.excursion import Excursion


class ExcursionService: 
    @staticmethod
    def validar_excursion(excursion: Excursion):
        """
        Valida una excursión.
        Lanza una excepción si la excursión no es válida.
        """
        if not excursion.lugar:
            raise ValueError("El lugar de la excursión no puede estar vacío.")
        if not excursion.fecha:
            raise ValueError("La fecha de la excursión no puede estar vacía.")
        if excursion.precio <= 0:
            raise ValueError("El precio de la excursión debe ser mayor a 0.")
        if excursion.disponibilidad_plazas <= 0:
            raise ValueError("La disponibilidad de plazas debe ser mayor a 0.")
        if not excursion.proveedor:
            raise ValueError("La excursión debe tener un proveedor asignado.")
        