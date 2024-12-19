from aplicacion.dtos.excursiondto import ExcursionDTO

class ExcursionMapper:
    @staticmethod
    def json_a_dto(data: dict) -> ExcursionDTO:
        return ExcursionDTO(
            id=data.get("id"),
            lugar=data.get("lugar"),
            fecha=data.get("fecha"),
            precio=data.get("precio"),
            disponibilidad_plazas=data.get("disponibilidad_plazas"),
            proveedor_id=data.get("proveedor_id"),
        )

    @staticmethod
    def dto_a_json(dto: ExcursionDTO) -> dict:
        return {
            "id": dto.id,
            "lugar": dto.lugar,
            "fecha": dto.fecha,
            "precio": dto.precio,
            "disponibilidad_plazas": dto.disponibilidad_plazas,
            "proveedor_id": dto.proveedor_id,
        }
