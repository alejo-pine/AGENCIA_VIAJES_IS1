from aplicacion.dtos.paquetedto import PaqueteDTO
from dominio.entidades.paqueteturistico import PaqueteTuristico
from dominio.repositorios.ipaqueterepositorio import IPaqueteRepository
from dominio.servicios.paqueteservicio import PaqueteService


class PaqueteApplicationService:
    def __init__(self, paquete_repository: IPaqueteRepository):
        """
        Constructor que recibe la implementación de IPaqueteRepository
        y la inicialización del PaqueteService.
        """
        self.paquete_repository = paquete_repository
        self.paquete_service = PaqueteService()

    def crear_paquete(self, paquete_dto: PaqueteDTO):
        """
        Caso de uso: Crear un nuevo paquete turístico.
        Transforma el DTO en una entidad PaqueteTuristico y lo guarda.
        """
        paquete = PaqueteTuristico(
            id=paquete_dto.id,
            nombre=paquete_dto.nombre,
            demanda=paquete_dto.demanda
        )
        self.paquete_service.ajustar_precio_por_demanda(paquete, paquete_dto.demanda)
        self.paquete_repository.guardar(paquete)

    def calcular_precio(self, paquete_id: str) -> float:
        """
        Caso de uso: Calcular el precio de un paquete turístico.
        """
        paquete = self.paquete_repository.buscar_por_id(paquete_id)
        return self.paquete_service.calcular_precio_paquete(paquete)