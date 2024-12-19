from aplicacion.dtos.hoteldto import HotelDTO

class HotelMapper:
    @staticmethod
    def json_a_dto(data: dict) -> HotelDTO:
        return HotelDTO(
            id=data.get("id"),
            nombre=data.get("nombre"),
            tipo_habitacion=data.get("tipo_habitacion"),
            disponibilidad_habitaciones=data.get("disponibilidad_habitaciones"),
            precio=data.get("precio"),
            proveedor_id=data.get("proveedor_id"),
        )

    @staticmethod
    def dto_a_json(dto: HotelDTO) -> dict:
        return {
            "id": dto.id,
            "nombre": dto.nombre,
            "tipo_habitacion": dto.tipo_habitacion,
            "disponibilidad_habitaciones": dto.disponibilidad_habitaciones,
            "precio": dto.precio,
            "proveedor_id": dto.proveedor_id,
        }
