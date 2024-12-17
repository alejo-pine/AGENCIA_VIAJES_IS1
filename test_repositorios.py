from dominio.entidades.paqueteturistico import PaqueteTuristico
from infraestructura.fabrica.repositorio_fabrica import RepositoryFactory
from dominio.entidades.cliente import Cliente
from dominio.entidades.proveedor import Proveedor
from dominio.entidades.factura import Factura
from datetime import datetime

def test_cliente_repository():
    print("\n--- Test Cliente Repository ---")
    cliente_repo = RepositoryFactory.get_cliente_repository()
    
    # Crear y guardar un cliente
    cliente = Cliente(
        id="C1",
        nombre="Juan Pérez",
        direccion="Calle 123",
        correo="juan@example.com",
        telefono="555-1234"
    )
    cliente_repo.guardar(cliente)
    print("Cliente guardado exitosamente.")
    
    # Buscar cliente por ID
    cliente_recuperado = cliente_repo.buscar_por_id("C1")
    print("Cliente recuperado:", cliente_recuperado)
    
    # Listar todos los clientes
    clientes = cliente_repo.listar_clientes()
    print("Lista de clientes:")
    for c in clientes:
        print(c)


def test_proveedor_repository():
    print("\n--- Test Proveedor Repository ---")
    proveedor_repo = RepositoryFactory.get_proveedor_repository()
    
    # Crear y guardar un proveedor
    proveedor = Proveedor(
        id="P1",
        nombre="Aerolínea Global",
        tipo="Transporte"
    )
    proveedor_repo.guardar(proveedor)
    print("Proveedor guardado exitosamente.")
    
    # Buscar proveedor por ID
    proveedor_recuperado = proveedor_repo.buscar_por_id("P1")
    print("Proveedor recuperado:", proveedor_recuperado)
    
    # Listar todos los proveedores
    proveedores = proveedor_repo.listar_proveedores()
    print("Lista de proveedores:")
    for p in proveedores:
        print(p)


def test_paquete_repository():
    print("\n--- Test Paquete Repository ---")
    paquete_repo = RepositoryFactory.get_paquete_repository()
    
    # Crear y guardar un paquete turístico
    paquete = PaqueteTuristico(
        id="PK1",
        nombre="Viaje a París",
        demanda=10.0
    )
    paquete.calcular_precio()  # Calcula un precio inicial si es necesario
    paquete_repo.guardar(paquete)
    print("Paquete guardado exitosamente.")
    
    # Buscar paquete por ID
    paquete_recuperado = paquete_repo.buscar_por_id("PK1")
    print("Paquete recuperado:", paquete_recuperado)
    
    # Listar todos los paquetes
    paquetes = paquete_repo.listar_paquetes()
    print("Lista de paquetes:")
    for p in paquetes:
        print(p)


def test_factura_repository():
    print("\n--- Test Factura Repository ---")
    factura_repo = RepositoryFactory.get_factura_repository()
    cliente_repo = RepositoryFactory.get_cliente_repository()
    paquete_repo = RepositoryFactory.get_paquete_repository()
    
    # Asegurarse de que existan un cliente y un paquete
    cliente = Cliente(id="C1", nombre="Juan Pérez", direccion="Calle 123", correo="juan@example.com", telefono="555-1234")
    paquete = PaqueteTuristico(id="PK1", nombre="Viaje a París", demanda=10.0)
    cliente_repo.guardar(cliente)
    paquete_repo.guardar(paquete)
    
    # Crear y guardar una factura
    factura = Factura(
        id="F1",
        numero_factura="FAC-001",
        fecha=datetime.now(),
        metodo_de_pago="Tarjeta de crédito",
        cliente=cliente,
        paquete=paquete
    )
    factura_repo.guardar(factura)
    print("Factura guardada exitosamente.")
    
    # Buscar factura por cliente ID
    facturas = factura_repo.buscar_por_cliente(cliente_id="C1")
    print("Facturas del cliente Juan Pérez:")
    for f in facturas:
        print(f)


if __name__ == "__main__":
    # Ejecutar pruebas para cada repositorio
    test_cliente_repository()
    test_proveedor_repository()
    test_paquete_repository()
    test_factura_repository()
