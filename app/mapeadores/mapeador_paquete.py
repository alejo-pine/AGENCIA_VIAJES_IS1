from aplicacion.dtos.paquetedto import PaqueteDTO

class PaqueteMapper:
    @staticmethod
    def json_a_dto(data: dict) -> PaqueteDTO:
        return PaqueteDTO(
            id=data.get("id"),
            nombre=data.get("nombre"),
            precio=data.get("precio"),
            demanda=data.get("demanda")
        )

    @staticmethod
    def dto_a_json(dto: PaqueteDTO) -> dict:
        return {
            "id": dto.id,
            "nombre": dto.nombre,
            "precio": dto.precio,
            "demanda": dto.demanda
        }
