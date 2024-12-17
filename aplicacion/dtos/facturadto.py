class FacturaDTO:
    def __init__(self, id: str, numero_factura: str, fecha: str, metodo_de_pago: str, total: float, cliente_id: str, paquete_id: str):
        self.id = id
        self.numero_factura = numero_factura
        self.fecha = fecha
        self.metodo_de_pago = metodo_de_pago
        self.total = total
        self.cliente_id = cliente_id
        self.paquete_id = paquete_id