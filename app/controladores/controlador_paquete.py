import os
from fastapi import APIRouter, HTTPException
from ..mapeadores.mapeador_paquete import PaqueteMapper
from aplicacion.servicios.paqueteaplicacionservicio import PaqueteApplicationService
from infraestructura.repositorios.sqlite_paquete_repository import SQLitePaqueteRepository
db_path = os.path.join("database.db")

# Crear el router para Paquetes
router = APIRouter()

# Inicializar el servicio con el repositorio
paquete_service = PaqueteApplicationService(SQLitePaqueteRepository(db_path))
paquete_mapper = PaqueteMapper()

@router.post("/paquetes/")
def crear_paquete(paquete_data: dict):
    """
    Endpoint para crear un nuevo paquete turístico.
    """
    try:
        paquete_dto = paquete_mapper.json_a_dto(paquete_data)
        paquete_service.crear_paquete(paquete_dto)
        return {"message": "Paquete turístico creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/paquetes/{paquete_id}/calcular-precio")
def calcular_precio(paquete_id: str):
    """
    Endpoint para calcular el precio de un paquete turístico por ID.
    """
    try:
        precio = paquete_service.calcular_precio(paquete_id)
        return {"paquete_id": paquete_id, "precio": precio}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/paquetes/")
def obtener_paquetes():
    """
    Endpoint para obtener la lista de paquetes turísticos.
    """
    try:
        paquetes = paquete_service.obtener_paquetes()
        return [paquete_mapper.dto_a_json(paquete) for paquete in paquetes]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

