import sqlite3
from typing import List
from dominio.entidades.vuelo import Vuelo
from dominio.repositorios.ivuelorepositorio import IVueloRepository
from dominio.repositorios.iproveedorrepositorio import IProveedorRepository

class SQLiteVueloRepository(IVueloRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.proveedor_repo = IProveedorRepository(db_path)

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def guardar(self, vuelo: Vuelo) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO vuelos (id, aerolinea, destino, fecha, disponibilidad_asientos, precio, proveedor_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (vuelo.id, vuelo.aerolinea, vuelo.destino, vuelo.fecha, vuelo.disponibilidad_asientos, vuelo.precio, vuelo.proveedor.id),
            )
            conn.commit()

    def buscar_por_id(self, id: str) -> Vuelo:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vuelos WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                proveedor = self.proveedor_repo.buscar_por_id(row["proveedor_id"])
                return Vuelo(
                    id=row["id"],
                    aerolinea=row["aerolinea"],
                    destino=row["destino"],
                    fecha=row["fecha"],
                    disponibilidad_asientos=row["disponibilidad_asientos"],
                    precio=row["precio"],
                    proveedor=proveedor
                )
            return None

    def listar_vuelos(self) -> List[Vuelo]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vuelos")
            rows = cursor.fetchall()
            return [
                Vuelo(
                    id=row["id"],
                    aerolinea=row["aerolinea"],
                    destino=row["destino"],
                    fecha=row["fecha"],
                    disponibilidad_asientos=row["disponibilidad_asientos"],
                    precio=row["precio"],
                    proveedor=self.proveedor_repo.buscar_por_id(row["proveedor_id"])
                )
                for row in rows
            ]
            
    def eliminar(self, id: str) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vuelos WHERE id = ?", (id,))
            conn.commit()
            
