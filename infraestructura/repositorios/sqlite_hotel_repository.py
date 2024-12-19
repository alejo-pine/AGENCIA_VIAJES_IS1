import sqlite3
from typing import List
from dominio.entidades.hotel import Hotel
from dominio.repositorios.ihotelrepositorio import IHotelRepository
from dominio.repositorios.iproveedorrepositorio import IProveedorRepository


class SQLiteHotelRepository(IHotelRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.proveedor_repo = IProveedorRepository(db_path)

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def guardar(self, hotel: Hotel) -> None:
        """
        Guarda un hotel en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO hoteles (id, nombre, tipo_habitacion, disponibilidad_habitaciones, precio, proveedor_id)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (hotel.id, hotel.nombre, hotel.tipo_habitacion, hotel.disponibilidad_habitaciones, hotel.precio, hotel.proveedor.id),
            )
            conn.commit()

    def buscar_por_id(self, id: str) -> Hotel:
        """
        Busca un hotel por su ID.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM hoteles WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                proveedor = self.proveedor_repo.buscar_por_id(row["proveedor_id"])
                return Hotel(
                    id=row["id"],
                    nombre=row["nombre"],
                    tipo_habitacion=row["tipo_habitacion"],
                    disponibilidad_habitaciones=row["disponibilidad_habitaciones"],
                    precio=row["precio"],
                    proveedor=proveedor
                )
            return None

    def listar_hoteles(self) -> List[Hotel]:
        """
        Lista todos los hoteles almacenados en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM hoteles")
            rows = cursor.fetchall()
            return [
                Hotel(
                    id=row["id"],
                    nombre=row["nombre"],
                    tipo_habitacion=row["tipo_habitacion"],
                    disponibilidad_habitaciones=row["disponibilidad_habitaciones"],
                    precio=row["precio"],
                    proveedor=self.proveedor_repo.buscar_por_id(row["proveedor_id"])
                )
                for row in rows
            ]
            
    def eliminar(self, id: str) -> None:
        """
        Elimina un hotel de la base de datos por su ID.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM hoteles WHERE id = ?", (id,))
            conn.commit()
