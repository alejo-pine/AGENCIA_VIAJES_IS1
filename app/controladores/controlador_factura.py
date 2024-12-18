import os
from fastapi import APIRouter, HTTPException
from ..mapeadores.mapeador_factura import FacturaMapper
from aplicacion.servicios.facturaaplicacionservicio import FacturaApplicationService
from infraestructura.repositorios.sqlite_factura_repository import SQLiteFacturaRepository
from infraestructura.repositorios.sqlite_cliente_repository import SQLiteClienteRepository
from infraestructura.repositorios.sqlite_paquete_repository import SQLitePaqueteRepository
db_path = os.path.join("database.db")

# Crear el router para Factura
router = APIRouter()

# Inicializar servicio con los repositorios necesarios
factura_service = FacturaApplicationService(
    SQLiteFacturaRepository(db_path),
    SQLiteClienteRepository(db_path),
    SQLitePaqueteRepository(db_path)
)
factura_mapper = FacturaMapper()

@router.post("/facturas/")
def generar_factura(factura_data: dict):
    try:
        factura_dto = factura_mapper.json_a_dto(factura_data)
        factura_service.generar_factura(factura_dto)
        return {"message": "Factura generada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
