from fastapi import APIRouter, HTTPException
from app.mapeadores.mapeador_proveedor import ProveedorMapper
from aplicacion.servicios.proveedoraplicacionservicio import ProveedorApplicationService
from infraestructura.repositorios.sqlite_proveedor_repository import SQLiteProveedorRepository

# Crear el router para Proveedores
router = APIRouter()

# Inicializar el servicio con el repositorio
proveedor_service = ProveedorApplicationService(SQLiteProveedorRepository())
proveedor_mapper = ProveedorMapper()

@router.post("/proveedores/")
def registrar_proveedor(proveedor_data: dict):
    """
    Endpoint para registrar un nuevo proveedor.
    """
    try:
        proveedor_dto = proveedor_mapper.json_a_dto(proveedor_data)
        proveedor_service.registrar_proveedor(proveedor_dto)
        return {"message": "Proveedor registrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/proveedores/{proveedor_id}/contratos/")
def registrar_contrato(proveedor_id: str, contrato_data: dict):
    """
    Endpoint para registrar un contrato asociado a un proveedor.
    """
    try:
        proveedor_service.registrar_contrato(proveedor_id, contrato_data)
        return {"message": "Contrato registrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/proveedores/{proveedor_id}/contratos/verificar-renovacion")
def verificar_renovacion_contratos(proveedor_id: str):
    """
    Endpoint para verificar si algún contrato del proveedor está próximo a vencerse.
    """
    try:
        renovacion_necesaria = proveedor_service.verificar_renovacion_contratos(proveedor_id)
        return {"proveedor_id": proveedor_id, "renovacion_necesaria": renovacion_necesaria}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
