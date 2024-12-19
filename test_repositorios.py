from infraestructura.fabrica.repositorio_fabrica import RepositoryFactory
from dominio.entidades.contrato import Contrato


def test_repositorio_contratos():
    contrato_repo = RepositoryFactory.get_contrato_repository()
    contrato_repo.eliminar("C1")
    contrato_repo.eliminar("C2")

    # Crear y guardar contratos
    contrato1 = Contrato(
        id="C1",
        fecha_inicio="2024-01-01",
        fecha_expiracion="2024-12-31",
        condiciones="Contrato anual con vuelos internacionales."
    )
    contrato_repo.guardar(contrato1, proveedor_id="P1")

    contrato2 = Contrato(
        id="C2",
        fecha_inicio="2024-06-01",
        fecha_expiracion="2025-05-31",
        condiciones="Contrato semestral para vuelos locales."
    )
    contrato_repo.guardar(contrato2, proveedor_id="P1")
    print("Contratos guardados exitosamente.")

    # Buscar contrato por ID
    contrato_recuperado = contrato_repo.buscar_por_id("C1")
    print("\nContrato Recuperado:")
    print(contrato_recuperado)

    # Listar todos los contratos
    print("\nLista de Contratos:")
    contratos = contrato_repo.listar_contratos()
    for contrato in contratos:
        print(contrato)

    # Listar contratos por proveedor
    print("\nContratos Asociados al Proveedor 'P1':")
    contratos_proveedor = contrato_repo.listar_contratos_por_proveedor("P1")
    for contrato in contratos_proveedor:
        print(contrato)


if __name__ == "__main__":
    test_repositorio_contratos()
