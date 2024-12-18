import sqlite3
from typing import List
from dominio.entidades.excursion import Excursion
from dominio.repositorios.iexcursionrepositorio import IExcursionRepository


class SQLiteExcursionRepository(IExcursionRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def guardar(self, excursion: Excursion) -> None:
        """
        Guarda una excursión en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO excursiones (id, lugar, fecha, precio, disponibilidad_plazas, proveedor_id)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (excursion.id, excursion.lugar, excursion.fecha, excursion.precio, excursion.disponibilidad_plazas, excursion.proveedor_id),
            )
            conn.commit()

    def buscar_por_id(self, id: str) -> Excursion:
        """
        Busca una excursión por su ID.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM excursiones WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return Excursion(
                    id=row["id"],
                    lugar=row["lugar"],
                    fecha=row["fecha"],
                    precio=row["precio"],
                    disponibilidad_plazas=row["disponibilidad_plazas"],
                    proveedor=row["proveedor_id"]
                )
            return None

    def listar_excursiones(self) -> List[Excursion]:
        """
        Lista todas las excursiones almacenadas en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM excursiones")
            rows = cursor.fetchall()
            return [
                Excursion(
                    id=row["id"],
                    lugar=row["lugar"],
                    fecha=row["fecha"],
                    precio=row["precio"],
                    disponibilidad_plazas=row["disponibilidad_plazas"],
                    proveedor=row["proveedor_id"]
                )
                for row in rows
            ]
