from aplicacion.dtos.clientedto import ClienteDTO

class ClienteMapper:
    @staticmethod
    def json_a_dto(data: dict) -> ClienteDTO:
        return ClienteDTO(
            id=data.get("id"),
            nombre=data.get("nombre"),
            direccion=data.get("direccion"),
            correo=data.get("correo"),
            telefono=data.get("telefono"),
        )

    @staticmethod
    def dto_a_json(dto: ClienteDTO) -> dict:
        return {
            "id": dto.id,
            "nombre": dto.nombre,
            "direccion": dto.direccion,
            "correo": dto.correo,
            "telefono": dto.telefono,
        }
