from dominio.entidades.proveedor import Proveedor


class Hotel:
    def __init__(self, id: str, nombre: str, tipo_habitacion: str, disponibilidad_habitaciones: int, precio: float, proveedor: Proveedor):
        self.id = id
        self.nombre = nombre
        self.tipo_habitacion = tipo_habitacion
        self.disponibilidad_habitaciones = disponibilidad_habitaciones
        self.precio = precio
        self.proveedor = proveedor

    def verificar_disponibilidad(self) -> bool:
        return self.disponibilidad_habitaciones > 0

    def actualizar_disponibilidad(self, cantidad: int) -> None:
        self.disponibilidad_habitaciones -= cantidad

    def __repr__(self):
        return f"Hotel({self.nombre}, {self.tipo_habitacion}, Disponibles: {self.disponibilidad_habitaciones})"
