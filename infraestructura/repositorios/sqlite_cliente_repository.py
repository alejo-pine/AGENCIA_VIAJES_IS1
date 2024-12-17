import sqlite3
from typing import List
from dominio.entidades.cliente import Cliente
from dominio.repositorios.iclienterepositorio import IClienteRepository


class SQLiteClienteRepository(IClienteRepository):
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

    def guardar(self, cliente: Cliente) -> None:
        """
        Guarda un nuevo cliente en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO clientes (nombre, direccion, correo, telefono)
                VALUES (?, ?, ?, ?)
                """,
                (cliente.nombre, cliente.direccion, cliente.correo, cliente.telefono),
            )
            conn.commit()

    def buscar_por_id(self, id: str) -> Cliente:
        """
        Busca un cliente por su ID en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return Cliente(
                    nombre=row["nombre"],
                    direccion=row["direccion"],
                    correo=row["correo"],
                    telefono=row["telefono"],
                )
            return None

    def listar_clientes(self) -> List[Cliente]:
        """
        Lista todos los clientes almacenados en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()
            return [
                Cliente(
                    id=row["id"],
                    nombre=row["nombre"],
                    direccion=row["direccion"],
                    correo=row["correo"],
                    telefono=row["telefono"],
                )
                for row in rows
            ]
            
    def eliminar(self, id: str) -> None:
        """
        Elimina un cliente por su ID de la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
            conn.commit()
