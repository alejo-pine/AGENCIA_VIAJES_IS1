from aplicacion.dtos.proveedordto import ProveedorDTO

class ProveedorMapper:
    @staticmethod
    def json_a_dto(data: dict) -> ProveedorDTO:
        """
        Convierte un diccionario JSON en un ProveedorDTO.
        """
        return ProveedorDTO(
            id=data.get("id"),
            nombre=data.get("nombre"),
            tipo=data.get("tipo")
        )

    @staticmethod
    def dto_a_json(dto: ProveedorDTO) -> dict:
        """
        Convierte un ProveedorDTO en un diccionario JSON.
        """
        return {
            "id": dto.id,
            "nombre": dto.nombre,
            "tipo": dto.tipo
        }
