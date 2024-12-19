import os
from fastapi import APIRouter, HTTPException
from ..mapeadores.mapeador_cliente import ClienteMapper
from aplicacion.servicios.clienteaplicacionservicio import ClienteApplicationService
from infraestructura.repositorios.sqlite_cliente_repository import SQLiteClienteRepository
db_path = os.path.join("database.db")
# Crear el router para Cliente
router = APIRouter()
# Inicializar servicio con el repositorio correspondiente
cliente_service = ClienteApplicationService(SQLiteClienteRepository(db_path))
cliente_mapper = ClienteMapper()

@router.post("/clientes/")
def registrar_cliente(cliente_data: dict):
    try:
        cliente_dto = cliente_mapper.json_a_dto(cliente_data)
        cliente_service.registrar_cliente(cliente_dto)  
        return {"message": "Cliente registrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/clientes/")
def obtener_clientes():
    try:
        clientes = cliente_service.obtener_clientes()
        return [cliente_mapper.dto_a_json(cliente) for cliente in clientes]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
