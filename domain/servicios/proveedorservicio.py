from domain.entidades.contrato import Contrato
from domain.entidades.proveedor import Proveedor


class ProveedorService:
    @staticmethod
    def registrar_contrato(proveedor: Proveedor, contrato: Contrato) -> None:
        """
        Registra un contrato nuevo con un proveedor.
        """
        proveedor.registrar_contrato(contrato)

    @staticmethod
    def verificar_renovacion_contratos(proveedor: Proveedor) -> bool:
        """
        Verifica si algún contrato del proveedor está próximo a vencerse.
        """
        return proveedor.alerta_renovacion_contrato()