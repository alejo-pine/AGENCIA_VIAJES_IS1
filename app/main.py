from fastapi import FastAPI
from controladores.controlador_cliente import router as cliente_router
from controladores.controlador_factura import router as factura_router
from controladores.controlador_paquete import router as paquete_router
from controladores.controlador_proveedor import router as proveedor_router

app = FastAPI()

# Registrar rutas
app.include_router(cliente_router, prefix="/api/v1")
app.include_router(factura_router, prefix="/api/v1")
app.include_router(paquete_router, prefix="/api/v1")
app.include_router(proveedor_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Bienvenido al sistema de gestión de proveedores y contratos!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
