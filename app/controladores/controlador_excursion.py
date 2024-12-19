import os
from fastapi import APIRouter, HTTPException
from ..mapeadores.mapeador_excursion import ExcursionMapper
from aplicacion.servicios.excursionaplicacionservicio import ExcursionApplicationService
from infraestructura.repositorios.sqlite_excursion_repository import SQLiteExcursionRepository

db_path = os.path.join("database.db")
router = APIRouter()

# Inicializar servicio con el repositorio correspondiente
excursion_service = ExcursionApplicationService(SQLiteExcursionRepository(db_path))
excursion_mapper = ExcursionMapper()

@router.post("/excursiones/")
def registrar_excursion(excursion_data: dict):
    try:
        excursion_dto = excursion_mapper.json_a_dto(excursion_data)
        excursion_service.registrar_excursion(excursion_dto)  
        return {"message": "Excursión registrada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/excursiones/")
def obtener_excursiones():
    try:
        excursiones = excursion_service.obtener_excursiones()
        return [excursion_mapper.dto_a_json(excursion) for excursion in excursiones]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
