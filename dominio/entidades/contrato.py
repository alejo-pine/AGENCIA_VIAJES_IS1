from datetime import datetime


class Contrato:
    def __init__(self, id: str, fecha_inicio: datetime, fecha_expiracion: datetime, condiciones: str):
        self.id = id
        self.fecha_inicio = fecha_inicio
        self.fecha_expiracion = fecha_expiracion
        self.condiciones = condiciones

    def verificar_renovacion(self) -> bool:
        return (self.fecha_expiracion - datetime.now()).days <= 30

    def __repr__(self):
        return f"Contrato(Expira: {self.fecha_expiracion})"