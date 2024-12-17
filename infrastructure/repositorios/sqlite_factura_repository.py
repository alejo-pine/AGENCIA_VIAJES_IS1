import sqlite3
from typing import List
from domain.entidades.factura import Factura
from domain.repositorios.ifacturarepositorio import IFacturaRepository


class SQLiteFacturaRepository(IFacturaRepository):
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

    def guardar(self, factura: Factura) -> None:
        """
        Guarda una nueva factura en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO facturas (numero_factura, fecha, metodo_pago, total, cliente_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                (factura.numero_factura, factura.fecha, factura.metodo_de_pago, factura.total, factura.cliente_id),
            )
            conn.commit()

    def buscar_por_cliente(self, cliente_id: str) -> List[Factura]:
        """
        Busca facturas por el ID del cliente.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facturas WHERE cliente_id = ?", (cliente_id,))
            rows = cursor.fetchall()
            return [
                Factura(
                    numero_factura=row["numero_factura"],
                    fecha=row["fecha"],
                    metodo_de_pago=row["metodo_pago"],
                    total=row["total"],
                    cliente_id=row["cliente_id"],
                )
                for row in rows
            ]

    def listar_facturas(self) -> List[Factura]:
        """
        Lista todas las facturas en la base de datos.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facturas")
            rows = cursor.fetchall()
            return [
                Factura(
                    numero_factura=row["numero_factura"],
                    fecha=row["fecha"],
                    metodo_de_pago=row["metodo_pago"],
                    total=row["total"],
                    cliente_id=row["cliente_id"],
                )
                for row in rows
            ]
