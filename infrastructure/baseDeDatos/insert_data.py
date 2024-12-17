import sqlite3



"solo un ejemplo no lo utilicen!!!!!!!!"











def insertar_datos():
    db_path = "database.db"  # Ruta de la base de datos

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Insertar un cliente
        cursor.execute(
            "INSERT INTO clientes (id, nombre, direccion, correo, telefono) VALUES (?, ?, ?, ?, ?)",
            ("1", "Juan Pérez", "Calle 123", "juan.perez@example.com", "555-1234")
        )

        # Insertar un paquete turístico
        cursor.execute(
            "INSERT INTO paquetes (id, nombre, precio, demanda) VALUES (?, ?, ?, ?)",
            ("1", "Paquete Caribe", 1500.0, 1.5)
        )

        # Insertar un proveedor
        cursor.execute(
            "INSERT INTO proveedores (id, nombre, tipo) VALUES (?, ?, ?)",
            ("1", "Hotel ABC", "Hotel")
        )

        conn.commit()
        print("Datos insertados correctamente.")

if __name__ == "__main__":
    insertar_datos()
