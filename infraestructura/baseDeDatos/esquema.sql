-- Tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    correo TEXT NOT NULL,
    telefono TEXT NOT NULL
);

-- Tabla de historial de viajes
CREATE TABLE IF NOT EXISTS historial_viajes (
    id TEXT PRIMARY KEY,
    fecha_viaje TEXT NOT NULL,
    estado TEXT NOT NULL,
    paquete_id TEXT NOT NULL,
    cliente_id TEXT NOT NULL,
    FOREIGN KEY (paquete_id) REFERENCES paquetes (id),
    FOREIGN KEY (cliente_id) REFERENCES clientes (id)
);

-- Tabla de paquetes turísticos
CREATE TABLE IF NOT EXISTS paquetes (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL DEFAULT 0.0,
    demanda REAL NOT NULL DEFAULT 0.0
);

-- Tabla de facturas
CREATE TABLE IF NOT EXISTS facturas (
    id TEXT PRIMARY KEY,
    numero_factura TEXT NOT NULL,
    fecha TEXT NOT NULL,
    metodo_pago TEXT NOT NULL,
    total REAL NOT NULL,
    cliente_id TEXT NOT NULL,
    paquete_id TEXT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes (id),
    FOREIGN KEY (paquete_id) REFERENCES paquetes (id)
);

-- Tabla de proveedores
CREATE TABLE IF NOT EXISTS proveedores (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL
);

-- Tabla de contratos
CREATE TABLE IF NOT EXISTS contratos (
    id TEXT PRIMARY KEY,
    fecha_inicio TEXT NOT NULL,
    fecha_expiracion TEXT NOT NULL,
    condiciones TEXT NOT NULL,
    proveedor_id TEXT NOT NULL,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores (id)
);

-- Tabla de excursiones
CREATE TABLE IF NOT EXISTS excursiones (
    id TEXT PRIMARY KEY,
    lugar TEXT NOT NULL,
    fecha TEXT NOT NULL,
    precio REAL NOT NULL,
    disponibilidad_plazas INTEGER NOT NULL,
    proveedor_id TEXT NOT NULL,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores (id)
);

-- Tabla de hoteles
CREATE TABLE IF NOT EXISTS hoteles (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    tipo_habitacion TEXT NOT NULL,
    disponibilidad_habitaciones INTEGER NOT NULL,
    precio REAL NOT NULL,
    proveedor_id TEXT NOT NULL,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores (id)
);

-- Tabla de vuelos
CREATE TABLE IF NOT EXISTS vuelos (
    id TEXT PRIMARY KEY,
    aerolinea TEXT NOT NULL,
    destino TEXT NOT NULL,
    fecha TEXT NOT NULL,
    disponibilidad_asientos INTEGER NOT NULL,
    precio REAL NOT NULL,
    proveedor_id TEXT NOT NULL,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores (id)
);

-- Tabla de relación entre paquetes y vuelos
CREATE TABLE IF NOT EXISTS paquetes_vuelos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paquete_id TEXT NOT NULL,
    vuelo_id TEXT NOT NULL,
    FOREIGN KEY (paquete_id) REFERENCES paquetes (id),
    FOREIGN KEY (vuelo_id) REFERENCES vuelos (id)
);

-- Tabla de relación entre paquetes y hoteles
CREATE TABLE IF NOT EXISTS paquetes_hoteles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paquete_id TEXT NOT NULL,
    hotel_id TEXT NOT NULL,
    FOREIGN KEY (paquete_id) REFERENCES paquetes (id),
    FOREIGN KEY (hotel_id) REFERENCES hoteles (id)
);

-- Tabla de relación entre paquetes y excursiones
CREATE TABLE IF NOT EXISTS paquetes_excursiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paquete_id TEXT NOT NULL,
    excursion_id TEXT NOT NULL,
    FOREIGN KEY (paquete_id) REFERENCES paquetes (id),
    FOREIGN KEY (excursion_id) REFERENCES excursiones (id)
);

