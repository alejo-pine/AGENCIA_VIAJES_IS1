from dominio.entidades.excursion import Excursion


class ExcursionDTO:
    def __init__(self, id: str, lugar: str, fecha: str, precio: float, disponibilidad_plazas: int, proveedor_id: str):
        self.id = id
        self.lugar = lugar
        self.fecha = fecha
        self.precio = precio
        self.disponibilidad_plazas = disponibilidad_plazas
        self.proveedor_id = proveedor_id

    @staticmethod
    def from_entity(excursion: Excursion) -> "ExcursionDTO":
        if not excursion or not excursion.proveedor or not excursion.proveedor.id:
            raise ValueError("Datos de la excursión o proveedor incompletos.")
        return ExcursionDTO(
            id=excursion.id,
            lugar=excursion.lugar,
            fecha=excursion.fecha,
            precio=excursion.precio,
            disponibilidad_plazas=excursion.disponibilidad_plazas,
            proveedor_id=excursion.proveedor.id
        )