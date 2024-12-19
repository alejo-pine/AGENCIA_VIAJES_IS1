

from aplicacion.dtos.hoteldto import HotelDTO
from dominio.entidades.hotel import Hotel
from dominio.repositorios.ihotelrepositorio import IHotelRepository
from dominio.repositorios.iproveedorrepositorio import IProveedorRepository
from dominio.servicios.hotelservicio import HotelService


class HotelApplicationService:
    def __init__(self, hotel_repository: IHotelRepository, proveedor_repository: IProveedorRepository):
        """
        Constructor que recibe la implementación de IHotelRepository
        y la inicialización del HotelService.
        """
        self.hotel_repository = hotel_repository
        self.proveedor_repository = proveedor_repository
        self.hotel_service = HotelService()

    def registrar_hotel(self, hotel_dto: HotelDTO):
        """
        Caso de uso: Registrar un nuevo hotel.
        Transforma el DTO en una entidad Hotel y lo guarda.
        """
        proveedor = self.proveedor_repository.buscar_por_id(hotel_dto.proveedor_id)
        if not proveedor:
            raise ValueError(f"Proveedor con ID {hotel_dto.proveedor_id} no encontrado.")

        hotel = Hotel(
            id=hotel_dto.id,
            nombre=hotel_dto.nombre,
            tipo_habitacion=hotel_dto.tipo_habitacion,
            disponibilidad_habitaciones=hotel_dto.disponibilidad_habitaciones,
            precio=hotel_dto.precio,
            proveedor=proveedor
        )

        # Validar hotel usando el servicio de dominio
        self.hotel_service.validar_hotel(hotel)

        # Guardar el hotel
        self.hotel_repository.guardar(hotel)

    def obtener_hoteles(self) -> list[HotelDTO]:
        """
        Caso de uso: Obtener una lista de hoteles existentes.
        Retorna una lista de HotelDTO.
        """
        hoteles = self.hotel_repository.listar_hoteles()
        return [
            HotelDTO.from_entity(hotel)
            for hotel in hoteles
        ]

    def obtener_hotel_por_id(self, hotel_id: str) -> HotelDTO:
        """
        Caso de uso: Obtener un hotel por su ID.
        Retorna un HotelDTO si el hotel existe.
        """
        hotel = self.hotel_repository.buscar_por_id(hotel_id)
        if not hotel:
            raise ValueError(f"Hotel con ID {hotel_id} no encontrado.")
        return HotelDTO.from_entity(hotel)

    def eliminar_hotel(self, hotel_id: str):
        """
        Caso de uso: Eliminar un hotel por su ID.
        """
        hotel = self.hotel_repository.buscar_por_id(hotel_id)
        if not hotel:
            raise ValueError(f"Hotel con ID {hotel_id} no encontrado.")
        self.hotel_repository.eliminar(hotel_id)