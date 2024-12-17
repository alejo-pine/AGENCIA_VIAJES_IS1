from fastapi import APIRouter, HTTPException
from mapeadores.mapeador_cliente import ClienteMapper
from aplicacion import ClienteApplicationService
from infraestructura.repositorios.sqlite_cliente_repository import SQLiteClientRepository

# Crear el router para Cliente
router = APIRouter()
# Inicializar servicio con el repositorio correspondiente
cliente_service = ClienteApplicationService(SQLiteClientRepository())
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
