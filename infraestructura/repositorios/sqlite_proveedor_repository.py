import sqlite3
from typing import List
from dominio.entidades.proveedor import Proveedor
from dominio.repositorios.iproveedorrepositorio import IProveedorRepository
from infraestructura.repositorios.sqlite_contrato_repository import SQLiteContratoRepository


class SQLiteProveedorRepository(IProveedorRepository):
    def __init__(self, db_path: str):
        """
        Constructor que inicializa la conexión a la base de datos.
        """
        self.db_path = db_path
        self.contrato_repo = SQLiteContratoRepository(db_path)

    def _connect(self):
        """
        Crea y retorna una conexión a la base de datos SQLite.
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
        return conn

    def guardar(self, proveedor: Proveedor) -> None:
        """
        Guarda un nuevo proveedor en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO proveedores (id, nombre, tipo)
                VALUES (?, ?, ?)
                """,
                (proveedor.id, proveedor.nombre, proveedor.tipo),
            )
            conn.commit()

    def buscar_por_id(self, id: str) -> Proveedor:
        """
        Busca un proveedor por su ID en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM proveedores WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                proveedor = Proveedor(
                    id=row["id"],
                    nombre=row["nombre"],
                    tipo=row["tipo"]
                )
                # Cargar los contratos asociados
                proveedor.contratos = self.contrato_repo.listar_contratos_por_proveedor(proveedor.id)
                return proveedor
            return None
        
    def listar_proveedores(self) -> List[Proveedor]:
        """
        Lista todos los proveedores almacenados en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM proveedores")
            rows = cursor.fetchall()
            proveedores = []
            for row in rows:
                proveedor = Proveedor(
                    id=row["id"],
                    nombre=row["nombre"],
                    tipo=row["tipo"]
                )
                # Cargar los contratos asociados
                proveedor.contratos = self.contrato_repo.listar_contratos_por_proveedor(proveedor.id)
                proveedores.append(proveedor)
            return proveedores
            
    def eliminar(self, id: str) -> None:
        """
        Elimina un proveedor de la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM proveedores WHERE id = ?", (id,))
            conn.commit()
