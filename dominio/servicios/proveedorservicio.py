from dominio.entidades.contrato import Contrato
from dominio.entidades.proveedor import Proveedor


class ProveedorService:
    
    @staticmethod
    def validar_proveedor(proveedor: Proveedor) -> None:
        """
        Valida que un proveedor tenga los datos necesarios.
        """
        if not proveedor.nombre:
            raise ValueError("El proveedor debe tener un nombre.")
        if not proveedor.tipo:
            raise ValueError("El proveedor debe tener un tipo.")
    
    @staticmethod
    def registrar_contrato(proveedor: Proveedor, contrato: Contrato) -> None:
        """
        Registra un contrato nuevo con un proveedor.
        """
        proveedor.registrar_contrato(contrato)
