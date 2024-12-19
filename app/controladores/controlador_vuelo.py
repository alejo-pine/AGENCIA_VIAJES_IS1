import os
from fastapi import APIRouter, HTTPException
from ..mapeadores.mapeador_vuelo import VueloMapper
from aplicacion.servicios.vueloaplicacionservicio import VueloApplicationService
from infraestructura.repositorios.sqlite_vuelo_repository import SQLiteVueloRepository

db_path = os.path.join("database.db")
router = APIRouter()

# Inicializar servicio con el repositorio correspondiente
vuelo_service = VueloApplicationService(SQLiteVueloRepository(db_path))
vuelo_mapper = VueloMapper()

@router.post("/vuelos/")
def registrar_vuelo(vuelo_data: dict):
    try:
        vuelo_dto = vuelo_mapper.json_a_dto(vuelo_data)
        vuelo_service.registrar_vuelo(vuelo_dto)  
        return {"message": "Vuelo registrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/vuelos/")
def obtener_vuelos():
    try:
        vuelos = vuelo_service.obtener_vuelos()
        return [vuelo_mapper.dto_a_json(vuelo) for vuelo in vuelos]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
