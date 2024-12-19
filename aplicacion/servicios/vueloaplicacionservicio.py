from aplicacion.dtos.vuelodto import VueloDTO
from dominio.entidades.vuelo import Vuelo
from dominio.repositorios.ivuelorepositorio import IVueloRepository
from dominio.repositorios.iproveedorrepositorio import IProveedorRepository
from dominio.servicios.vueloservicio import VueloService
from dominio.entidades.proveedor import Proveedor


class VueloApplicationService:
    def __init__(self, vuelo_repository: IVueloRepository, proveedor_repository: IProveedorRepository):
        """
        Constructor que recibe la implementación de IVueloRepository
        y la inicialización del VueloService.
        """
        self.vuelo_repository = vuelo_repository
        self.proveedor_repository = proveedor_repository
        self.vuelo_service = VueloService()

    def registrar_vuelo(self, vuelo_dto: VueloDTO):
        """
        Caso de uso: Registrar un nuevo vuelo.
        Transforma el DTO en una entidad Vuelo y lo guarda.
        """
        proveedor = self.proveedor_repository.buscar_por_id(vuelo_dto.proveedor_id)
        if not proveedor:
            raise ValueError(f"Proveedor con ID {vuelo_dto.proveedor_id} no encontrado.")

        vuelo = Vuelo(
            id=vuelo_dto.id,
            aerolinea=vuelo_dto.aerolinea,
            destino=vuelo_dto.destino,
            fecha=vuelo_dto.fecha,
            disponibilidad_asientos=vuelo_dto.disponibilidad_asientos,
            precio=vuelo_dto.precio,
            proveedor=proveedor
        )

        # Validar vuelo usando el servicio de dominio
        self.vuelo_service.validar_vuelo(vuelo)

        # Guardar el vuelo
        self.vuelo_repository.guardar(vuelo)

    def obtener_vuelos(self) -> list[VueloDTO]:
        """
        Caso de uso: Obtener una lista de vuelos existentes.
        Retorna una lista de VueloDTO.
        """
        vuelos = self.vuelo_repository.listar_vuelos()
        return [
            VueloDTO.from_entity(vuelo)
            for vuelo in vuelos
        ]

    def obtener_vuelo_por_id(self, vuelo_id: str) -> VueloDTO:
        """
        Caso de uso: Obtener un vuelo por su ID.
        Retorna un VueloDTO si el vuelo existe.
        """
        vuelo = self.vuelo_repository.buscar_por_id(vuelo_id)
        if not vuelo:
            raise ValueError(f"Vuelo con ID {vuelo_id} no encontrado.")
        return VueloDTO.from_entity(vuelo)


    def eliminar_vuelo(self, vuelo_id: str):
        """
        Caso de uso: Eliminar un vuelo por su ID.
        """
        vuelo = self.vuelo_repository.buscar_por_id(vuelo_id)
        if not vuelo:
            raise ValueError(f"Vuelo con ID {vuelo_id} no encontrado.")
        self.vuelo_repository.eliminar(vuelo_id)
