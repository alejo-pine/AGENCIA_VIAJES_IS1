from dominio.entidades.hotel import Hotel


class HotelDTO:
    def __init__(self, id: str, nombre: str, tipo_habitacion: str, disponibilidad_habitaciones: int, precio: float, proveedor_id: str):
        self.id = id
        self.nombre = nombre
        self.tipo_habitacion = tipo_habitacion
        self.disponibilidad_habitaciones = disponibilidad_habitaciones
        self.precio = precio
        self.proveedor_id = proveedor_id

    @staticmethod
    def from_entity(hotel: Hotel) -> "HotelDTO":
        if not hotel or not hotel.proveedor or not hotel.proveedor.id:
            raise ValueError("Datos del hotel o proveedor incompletos.")
        return HotelDTO(
            id=hotel.id,
            nombre=hotel.nombre,
            tipo_habitacion=hotel.tipo_habitacion,
            disponibilidad_habitaciones=hotel.disponibilidad_habitaciones,
            precio=hotel.precio,
            proveedor_id=hotel.proveedor.id
        )