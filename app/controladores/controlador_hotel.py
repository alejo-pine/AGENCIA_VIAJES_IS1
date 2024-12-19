import os
from fastapi import APIRouter, HTTPException
from ..mapeadores.mapeador_hotel import HotelMapper
from aplicacion.servicios.hotelaplicacionservicio import HotelApplicationService
from infraestructura.repositorios.sqlite_hotel_repository import SQLiteHotelRepository

db_path = os.path.join("database.db")
router = APIRouter()

# Inicializar servicio con el repositorio correspondiente
hotel_service = HotelApplicationService(SQLiteHotelRepository(db_path))
hotel_mapper = HotelMapper()

@router.post("/hoteles/")
def registrar_hotel(hotel_data: dict):
    try:
        hotel_dto = hotel_mapper.json_a_dto(hotel_data)
        hotel_service.registrar_hotel(hotel_dto)  
        return {"message": "Hotel registrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/hoteles/")
def obtener_hoteles():
    try:
        hoteles = hotel_service.obtener_hoteles()
        return [hotel_mapper.dto_a_json(hotel) for hotel in hoteles]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
