from infraestructura.repositorios.sqlite_cliente_repository import SQLiteClienteRepository
from infraestructura.repositorios.sqlite_factura_repository import SQLiteFacturaRepository
from infraestructura.repositorios.sqlite_paquete_repository import SQLitePaqueteRepository
from infraestructura.repositorios.sqlite_proveedor_repository import SQLiteProveedorRepository


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
