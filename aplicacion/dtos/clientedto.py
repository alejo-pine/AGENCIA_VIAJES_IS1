class ClienteDTO:
    def __init__(self, id: str, nombre: str, direccion: str, correo: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono