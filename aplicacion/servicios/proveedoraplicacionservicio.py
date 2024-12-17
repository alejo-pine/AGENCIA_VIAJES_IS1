from aplicacion.dtos.proveedordto import ProveedorDTO
from dominio.entidades.contrato import Contrato
from dominio.entidades.proveedor import Proveedor
from dominio.repositorios.iproveedorrepositorio import IProveedorRepository
from dominio.servicios.proveedorservicio import ProveedorService


class ProveedorApplicationService:
    def __init__(self, proveedor_repository: IProveedorRepository):
        """
        Constructor que recibe la implementación de IProveedorRepository
        y la inicialización del ProveedorService.
        """
        self.proveedor_repository = proveedor_repository
        self.proveedor_service = ProveedorService()

    def registrar_proveedor(self, proveedor_dto: ProveedorDTO):
        """
        Caso de uso: Registrar un nuevo proveedor.
        Transforma el DTO en una entidad Proveedor y lo guarda.
        """
        proveedor = Proveedor(
            id=proveedor_dto.id,
            nombre=proveedor_dto.nombre,
            tipo=proveedor_dto.tipo
        )
        self.proveedor_repository.guardar(proveedor)

    def registrar_contrato(self, proveedor_id: str, contrato_data: dict):
        """
        Caso de uso: Registrar un contrato asociado a un proveedor.
        Recibe un diccionario con los datos del contrato.
        """
        proveedor = self.proveedor_repository.buscar_por_id(proveedor_id)
        contrato = Contrato(
            id=contrato_data['id'],
            fecha_inicio=contrato_data['fecha_inicio'],
            fecha_expiracion=contrato_data['fecha_expiracion'],
            condiciones=contrato_data['condiciones']
        )
        self.proveedor_service.registrar_contrato(proveedor, contrato)
        self.proveedor_repository.guardar(proveedor)

    def verificar_renovacion_contratos(self, proveedor_id: str) -> bool:
        """
        Caso de uso: Verificar si algún contrato del proveedor está próximo a vencerse.
        """
        proveedor = self.proveedor_repository.buscar_por_id(proveedor_id)
        return self.proveedor_service.verificar_renovacion_contratos(proveedor)