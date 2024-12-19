from aplicacion.dtos.facturadto import FacturaDTO

class FacturaMapper:
    @staticmethod
    def json_a_dto(data: dict) -> FacturaDTO:
        return FacturaDTO(
            id=data.get("id"),
            numero_factura=data.get("numero_factura"),
            fecha=data.get("fecha"),
            metodo_de_pago=data.get("metodo_de_pago"),
            total=data.get("total"),
            cliente_id=data.get("cliente_id"),
            paquete_id=data.get("paquete_id")
        )

    @staticmethod
    def dto_a_json(dto: FacturaDTO) -> dict:
        return {
            "id": dto.id,
            "numero_factura": dto.numero_factura,
            "fecha": dto.fecha,
            "metodo_de_pago": dto.metodo_de_pago,
            "total": dto.total,
            "cliente_id": dto.cliente_id,
            "paquete_id": dto.paquete_id
        }
