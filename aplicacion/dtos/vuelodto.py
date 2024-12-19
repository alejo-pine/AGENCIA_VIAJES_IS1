from dominio.entidades.vuelo import Vuelo


class VueloDTO:
    def __init__(self, id: str, aerolinea: str, destino: str, fecha: str, disponibilidad_asientos: int, precio: float, proveedor_id: str):
        self.id = id
        self.aerolinea = aerolinea
        self.destino = destino
        self.fecha = fecha
        self.disponibilidad_asientos = disponibilidad_asientos
        self.precio = precio
        self.proveedor_id = proveedor_id
        
    @staticmethod
    def from_entity(vuelo: Vuelo) -> "VueloDTO":
        """
        Crea un DTO a partir de una entidad de dominio.
        """
        if not vuelo:
            raise ValueError("El vuelo proporcionado es None.")
        if not vuelo.proveedor or not hasattr(vuelo.proveedor, "id"):
            raise ValueError("El proveedor del vuelo no es válido o está ausente.")

        return VueloDTO(
            id=vuelo.id,
            aerolinea=vuelo.aerolinea,
            destino=vuelo.destino,
            fecha=vuelo.fecha,
            disponibilidad_asientos=vuelo.disponibilidad_asientos,
            precio=vuelo.precio,
            proveedor_id=vuelo.proveedor.id  # Extraemos solo el ID del proveedor
        )