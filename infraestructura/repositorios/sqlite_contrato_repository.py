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

    def guardar(self, contrato: Contrato, proveedor_id: str) -> None:
        """
        Guarda un contrato en la base de datos, asociándolo a un proveedor.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO contratos (id, fecha_inicio, fecha_expiracion, condiciones, proveedor_id)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    fecha_inicio = excluded.fecha_inicio,
                    fecha_expiracion = excluded.fecha_expiracion,
                    condiciones = excluded.condiciones,
                    proveedor_id = excluded.proveedor_id
                """,
                (contrato.id, contrato.fecha_inicio, contrato.fecha_expiracion, contrato.condiciones, proveedor_id),
            )
            conn.commit()
            
    def buscar_por_id(self, id: str) -> Contrato:
        """
        Busca un contrato por su ID en la base de datos.
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
                    condiciones=row["condiciones"]
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
                    condiciones=row["condiciones"]
                )
                for row in rows
            ]

    def listar_contratos_por_proveedor(self, proveedor_id: str) -> List[Contrato]:
        """
        Lista todos los contratos asociados a un proveedor.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contratos WHERE proveedor_id = ?", (proveedor_id,))
            rows = cursor.fetchall()
            return [
                Contrato(
                    id=row["id"],
                    fecha_inicio=row["fecha_inicio"],
                    fecha_expiracion=row["fecha_expiracion"],
                    condiciones=row["condiciones"]
                )
                for row in rows
            ]
        
    def eliminar(self, id: str) -> None:
        """
        Elimina un contrato de la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contratos WHERE id = ?", (id,))
            conn.commit()       
