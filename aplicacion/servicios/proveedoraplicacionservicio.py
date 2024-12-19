from aplicacion.dtos.proveedordto import ProveedorDTO
from aplicacion.dtos.contratodto import ContratoDTO
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
        
        self.proveedor_service.validar_proveedor(proveedor)
        self.proveedor_repository.guardar(proveedor)

    def registrar_contrato(self, proveedor_id: str, contrato_dto: ContratoDTO):
        """
        Caso de uso: Registrar un contrato asociado a un proveedor.
        Recibe un ContratoDTO con los datos del contrato.
        """
        proveedor = self.proveedor_repository.buscar_por_id(proveedor_id)
        if not proveedor:
            raise ValueError(f"Proveedor con ID {proveedor_id} no encontrado.")

        # Convertir DTO a una entidad Contrato
        contrato = Contrato(
            id=contrato_dto.id,
            fecha_inicio=contrato_dto.fecha_inicio,
            fecha_expiracion=contrato_dto.fecha_expiracion,
            condiciones=contrato_dto.condiciones
        )

        # Registrar el contrato usando el servicio de dominio
        self.proveedor_service.registrar_contrato(proveedor, contrato)

        # Persistir el proveedor actualizado
        self.proveedor_repository.guardar(proveedor)

        
    def listar_proveedores(self) -> list[ProveedorDTO]:
        """
        Caso de uso: Listar todos los proveedores.
        Retorna una lista de DTOs.
        """
        proveedores = self.proveedor_repository.listar_proveedores()
        return [
            ProveedorDTO(
                id=proveedor.id,
                nombre=proveedor.nombre,
                tipo=proveedor.tipo
            ) for proveedor in proveedores
        ]
        
    def buscar_proveedor_por_id(self, proveedor_id: str) -> ProveedorDTO:
        """
        Caso de uso: Buscar un proveedor por su ID.
        Retorna un DTO con los datos del proveedor.
        """
        proveedor = self.proveedor_repository.buscar_por_id(proveedor_id)
        if not proveedor:
            raise ValueError(f"Proveedor con ID {proveedor_id} no encontrado.")
        
        return ProveedorDTO(
            id=proveedor.id,
            nombre=proveedor.nombre,
            tipo=proveedor.tipo
        )
        
    def eliminar_proveedor(self, proveedor_id: str):
        """
        Caso de uso: Eliminar un proveedor por su ID.
        """
        proveedor = self.proveedor_repository.buscar_por_id(proveedor_id)
        if not proveedor:
            raise ValueError(f"Proveedor con ID {proveedor_id} no encontrado.")
        self.proveedor_repository.eliminar(proveedor_id)
        
        
    