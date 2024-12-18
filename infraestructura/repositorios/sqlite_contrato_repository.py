import sqlite3
from typing import List
from dominio.entidades.contrato import Contrato
from dominio.repositorios.icontratorepositorio import IContratoRepository


class SQLiteContratoRepository(IContratoRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def guardar(self, contrato: Contrato) -> None:
        """
        Guarda un contrato en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO contratos (id, fecha_inicio, fecha_expiracion, condiciones)
                VALUES (?, ?, ?, ?)
                """,
                (contrato.id, contrato.fecha_inicio, contrato.fecha_expiracion, contrato.condiciones),
            )
            conn.commit()

    def buscar_por_id(self, id: str) -> Contrato:
        """
        Busca un contrato por su ID.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contratos WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return Contrato(
                    id=row["id"],
                    fecha_inicio=row["fecha_inicio"],
                    fecha_expiracion=row["fecha_expiracion"],
                    condiciones=row["condiciones"],
                    proveedor_id=row["proveedor_id"]
                )
            return None

    def listar_contratos(self) -> List[Contrato]:
        """
        Lista todos los contratos almacenados en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contratos")
            rows = cursor.fetchall()
            return [
                Contrato(
                    id=row["id"],
                    fecha_inicio=row["fecha_inicio"],
                    fecha_expiracion=row["fecha_expiracion"],
                    condiciones=row["condiciones"],
                    proveedor_id=row["proveedor_id"]
                )
                for row in rows
            ]
