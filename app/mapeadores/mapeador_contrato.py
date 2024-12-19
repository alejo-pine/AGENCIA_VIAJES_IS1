from aplicacion.dtos.contratodto import ContratoDTO

class ContratoMapper:
    @staticmethod
    def json_a_dto(data: dict) -> ContratoDTO:
        return ContratoDTO(
            id=data.get("id"),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_expiracion=data.get("fecha_expiracion"),
            condiciones=data.get("condiciones"),
        )

    @staticmethod
    def dto_a_json(dto: ContratoDTO) -> dict:
        return {
            "id": dto.id,
            "fecha_inicio": dto.fecha_inicio,
            "fecha_expiracion": dto.fecha_expiracion,
            "condiciones": dto.condiciones,
        }
