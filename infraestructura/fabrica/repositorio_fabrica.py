from infraestructura.repositorios.sqlite_cliente_repository import SQLiteClienteRepository
from infraestructura.repositorios.sqlite_factura_repository import SQLiteFacturaRepository
from infraestructura.repositorios.sqlite_paquete_repository import SQLitePaqueteRepository
from infraestructura.repositorios.sqlite_proveedor_repository import SQLiteProveedorRepository
from infraestructura.repositorios.sqlite_vuelo_repository import SQLiteVueloRepository
from infraestructura.repositorios.sqlite_excursion_repository import SQLiteExcursionRepository
from infraestructura.repositorios.sqlite_hotel_repository import SQLiteHotelRepository
from infraestructura.repositorios.sqlite_contrato_repository import SQLiteContratoRepository


class RepositoryFactory:
    DB_PATH = "database.db"  # Ruta centralizada de la base de datos

    @staticmethod
    def get_cliente_repository():
        """
        Devuelve una instancia del repositorio de clientes con SQLite.
        """
        return SQLiteClienteRepository(RepositoryFactory.DB_PATH)

    @staticmethod
    def get_factura_repository():
        """
        Devuelve una instancia del repositorio de facturas con SQLite.
        """
        return SQLiteFacturaRepository(RepositoryFactory.DB_PATH)

    @staticmethod
    def get_paquete_repository():
        """
        Devuelve una instancia del repositorio de paquetes turísticos con SQLite.
        """
        return SQLitePaqueteRepository(RepositoryFactory.DB_PATH)

    @staticmethod
    def get_proveedor_repository():
        """
        Devuelve una instancia del repositorio de proveedores con SQLite.
        """
        return SQLiteProveedorRepository(RepositoryFactory.DB_PATH)
    
    @staticmethod
    def get_vuelo_repository():
        """
        Devuelve una instancia del repositorio de vuelos con SQLite.
        """
        return SQLiteVueloRepository(RepositoryFactory.DB_PATH)
    
    @staticmethod
    def get_excursion_repository():
        """
        Devuelve una instancia del repositorio de excursiones con SQLite.
        """
        return SQLiteExcursionRepository(RepositoryFactory.DB_PATH)
    
    @staticmethod
    def get_hotel_repository():
        """
        Devuelve una instancia del repositorio de hoteles con SQLite.
        """
        return SQLiteHotelRepository(RepositoryFactory.DB_PATH)
    
    @staticmethod
    def get_contrato_repository():
        """
        Devuelve una instancia del repositorio de contratos con SQLite.
        """
        return SQLiteContratoRepository(RepositoryFactory.DB_PATH)
