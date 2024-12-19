from aplicacion.dtos.excursiondto import ExcursionDTO
from dominio.entidades.excursion import Excursion
from dominio.repositorios.iexcursionrepositorio import IExcursionRepository
from dominio.repositorios.iproveedorrepositorio import IProveedorRepository
from dominio.servicios.excursionservicio import ExcursionService


class ExcursionApplicationService:
    def __init__(self, excursion_repository: IExcursionRepository, proveedor_repository: IProveedorRepository):
        """
        Constructor que recibe la implementación de IExcursionRepository
        y la inicialización del ExcursionService.
        """
        self.excursion_repository = excursion_repository
        self.proveedor_repository = proveedor_repository
        self.excursion_service = ExcursionService()

    def registrar_excursion(self, excursion_dto: ExcursionDTO):
        """
        Caso de uso: Registrar una nueva excursión.
        Transforma el DTO en una entidad Excursion y lo guarda.
        """
        proveedor = self.proveedor_repository.buscar_por_id(excursion_dto.proveedor_id)
        if not proveedor:
            raise ValueError(f"Proveedor con ID {excursion_dto.proveedor_id} no encontrado.")

        excursion = Excursion(
            id=excursion_dto.id,
            lugar=excursion_dto.lugar,
            fecha=excursion_dto.fecha,
            precio=excursion_dto.precio,
            disponibilidad_plazas=excursion_dto.disponibilidad_plazas,
            proveedor=proveedor
        )

        # Validar excursión usando el servicio de dominio
        self.excursion_service.validar_excursion(excursion)

        # Guardar la excursión
        self.excursion_repository.guardar(excursion)

    def obtener_excursiones(self) -> list[ExcursionDTO]:
        """
        Caso de uso: Obtener una lista de excursiones existentes.
        Retorna una lista de ExcursionDTO.
        """
        excursiones = self.excursion_repository.listar_excursiones()
        return [
            ExcursionDTO.from_entity(excursion)
            for excursion in excursiones
        ]

    def obtener_excursion_por_id(self, excursion_id: str) -> ExcursionDTO:
        """
        Caso de uso: Obtener una excursión por su ID.
        Retorna un ExcursionDTO si la excursión existe.
        """
        excursion = self.excursion_repository.buscar_por_id(excursion_id)
        if not excursion:
            raise ValueError(f"Excursión con ID {excursion_id} no encontrada.")
        return ExcursionDTO.from_entity(excursion)

    def eliminar_excursion(self, excursion_id: str):
        """
        Caso de uso: Eliminar una excursión por su ID.
        """
        excursion = self.excursion_repository.buscar_por_id(excursion_id)
        if not excursion:
            raise ValueError(f"Excursión con ID {excursion_id} no encontrada.")
        self.excursion_repository.eliminar(excursion_id)