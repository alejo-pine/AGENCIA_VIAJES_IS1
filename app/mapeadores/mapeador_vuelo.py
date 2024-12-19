from aplicacion.dtos.vuelodto import VueloDTO

class VueloMapper:
    @staticmethod
    def json_a_dto(data: dict) -> VueloDTO:
        return VueloDTO(
            id=data.get("id"),
            aerolinea=data.get("aerolinea"),
            destino=data.get("destino"),
            fecha=data.get("fecha"),
            disponibilidad_asientos=data.get("disponibilidad_asientos"),
            precio=data.get("precio"),
            proveedor_id=data.get("proveedor_id"),
        )

    @staticmethod
    def dto_a_json(dto: VueloDTO) -> dict:
        return {
            "id": dto.id,
            "aerolinea": dto.aerolinea,
            "destino": dto.destino,
            "fecha": dto.fecha,
            "disponibilidad_asientos": dto.disponibilidad_asientos,
            "precio": dto.precio,
            "proveedor_id": dto.proveedor_id,
        }
