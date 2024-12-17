from aplicacion.dtos.clientedto import ClienteDTO
from dominio.entidades.cliente import Cliente
from dominio.repositorios.iclienterepositorio import IClienteRepository
from dominio.servicios.clienteservicio import ClienteService


class ClienteApplicationService:
    
    def __init__(self, cliente_repository: IClienteRepository):
        """
        Constructor que recibe la implementación de IClienteRepository
        y la inicialización del ClienteService.
        """
        self.cliente_repository = cliente_repository
        self.cliente_service = ClienteService()

    def registrar_cliente(self, cliente_dto: ClienteDTO):
        """
        Caso de uso: Registrar un nuevo cliente.
        Transforma el DTO en una entidad Cliente y delega la lógica al ClienteService.
        """
        cliente = Cliente(
            id=cliente_dto.id,
            nombre=cliente_dto.nombre,
            direccion=cliente_dto.direccion,
            correo=cliente_dto.correo,
            telefono=cliente_dto.telefono
        )
        self.cliente_service.validar_cliente(cliente)  # Validación lógica
        self.cliente_repository.guardar(cliente)       # Persistencia del cliente

    def obtener_clientes(self) -> list[ClienteDTO]:
        """
        Caso de uso: Obtener una lista de clientes existentes.
        Retorna una lista de ClienteDTO.
        """
        clientes = self.cliente_repository.listar_clientes()
        return [
            ClienteDTO(
                id=cliente.id,
                nombre=cliente.nombre,
                direccion=cliente.direccion,
                correo=cliente.correo,
                telefono=cliente.telefono
            ) for cliente in clientes
        ]