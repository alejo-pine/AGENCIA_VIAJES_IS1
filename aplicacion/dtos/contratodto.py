class ContratoDTO:
    def __init__(self, id: str, fecha_inicio: str, fecha_expiracion: str, condiciones: str):
        self.id = id
        self.fecha_inicio = fecha_inicio
        self.fecha_expiracion = fecha_expiracion
        self.condiciones = condiciones