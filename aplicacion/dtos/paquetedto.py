class PaqueteDTO:
    def __init__(self, id: str, nombre: str, precio: float, demanda: float):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.demanda = demanda