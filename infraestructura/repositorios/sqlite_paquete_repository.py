import sqlite3
from typing import List
from dominio.entidades.paqueteturistico import PaqueteTuristico
from dominio.repositorios.ipaqueterepositorio import IPaqueteRepository


class SQLitePaqueteRepository(IPaqueteRepository):
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

    def guardar(self, paquete: PaqueteTuristico) -> None:
        """
        Guarda un nuevo paquete turístico en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO paquetes (nombre, precio, demanda)
                VALUES (?, ?, ?)
                """,
                (paquete.nombre, paquete.precio, paquete.demanda),
            )
            conn.commit()

    def buscar_por_id(self, id: str) -> PaqueteTuristico:
        """
        Busca un paquete turístico por su ID en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM paquetes WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return PaqueteTuristico(
                    nombre=row["nombre"],
                    precio=row["precio"],
                    demanda=row["demanda"],
                    vuelos=[],  # Implementar si se almacenan vuelos
                    hoteles=[],  # Implementar si se almacenan hoteles
                    excursiones=[],  # Implementar si se almacenan excursiones
                )
            return None

    def listar_paquetes(self) -> List[PaqueteTuristico]:
        """
        Lista todos los paquetes turísticos almacenados en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM paquetes")
            rows = cursor.fetchall()
            return [
                PaqueteTuristico(
                    id=row["id"],
                    nombre=row["nombre"],
                    demanda=row["demanda"],
                    #vuelos=[],  # Implementar si se almacenan vuelos
                    #hoteles=[],  # Implementar si se almacenan hoteles
                    #excursiones=[],  # Implementar si se almacenan excursiones
                )
                for row in rows
            ]
            
    def eliminar(self, id: str) -> None:
        """
        Elimina un paquete turístico de la base de datos por su ID.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM paquetes WHERE id = ?", (id,))
            conn.commit()
