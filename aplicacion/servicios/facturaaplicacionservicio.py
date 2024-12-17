import datetime
from aplicacion.dtos.facturadto import FacturaDTO
from dominio.entidades.factura import Factura
from dominio.repositorios.iclienterepositorio import IClienteRepository
from dominio.repositorios.ifacturarepositorio import IFacturaRepository
from dominio.repositorios.ipaqueterepositorio import IPaqueteRepository


class FacturaApplicationService:
    def __init__(self, factura_repository: IFacturaRepository, cliente_repository: IClienteRepository, paquete_repository: IPaqueteRepository):
        """
        Constructor que recibe las implementaciones de los repositorios necesarios.
        """
        self.factura_repository = factura_repository
        self.cliente_repository = cliente_repository
        self.paquete_repository = paquete_repository

    def generar_factura(self, factura_dto: FacturaDTO):
        """
        Caso de uso: Generar una factura para un cliente asociado a un paquete turístico.
        """
        cliente = self.cliente_repository.buscar_por_id(factura_dto.cliente_id)
        paquete = self.paquete_repository.buscar_por_id(factura_dto.paquete_id)

        factura = Factura(
            id=factura_dto.id,
            numero_factura=factura_dto.numero_factura,
            fecha=datetime.now(),
            metodo_de_pago=factura_dto.metodo_de_pago,
            cliente=cliente,
            paquete=paquete
        )
        self.factura_repository.guardar(factura)