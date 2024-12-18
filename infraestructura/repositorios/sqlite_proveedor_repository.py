import sqlite3
from typing import List
from dominio.entidades.proveedor import Proveedor
from dominio.repositorios.iproveedorrepositorio import IProveedorRepository


class SQLiteProveedorRepository(IProveedorRepository):
    def __init__(self, db_path: str):
        """
        Constructor que inicializa la conexión a la base de datos.
        """
        self.db_path = db_path

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
                return Proveedor(
                    id=row["id"],
                    nombre=row["nombre"],
                    tipo=row["tipo"],
                )
            return None

    def listar_proveedores(self) -> List[Proveedor]:
        """
        Lista todos los proveedores almacenados en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM proveedores")
            rows = cursor.fetchall()
            return [
                Proveedor(
                    id=row["id"],
                    nombre=row["nombre"],
                    tipo=row["tipo"],
                )
                for row in rows
            ]
            
    def eliminar(self, id: str) -> None:
        """
        Elimina un proveedor de la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM proveedores WHERE id = ?", (id,))
            conn.commit()
