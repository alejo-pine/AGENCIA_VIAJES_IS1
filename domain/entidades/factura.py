from datetime import datetime

from domain.entidades.cliente import Cliente
from domain.entidades.paqueteturistico import PaqueteTuristico


class Factura:
    def __init__(self, id: str, numero_factura: str, fecha: datetime, metodo_de_pago: str, cliente: Cliente, paquete: PaqueteTuristico):
        self.id = id
        self.numero_factura = numero_factura
        self.fecha = fecha
        self.metodo_de_pago = metodo_de_pago
        self.total = paquete.calcular_precio()
        self.cliente = cliente
        self.paquete = paquete

    def __repr__(self):
        return f"Factura({self.numero_factura}, Total: {self.total}, Cliente: {self.cliente.nombre})"