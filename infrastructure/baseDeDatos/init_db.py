import sqlite3

def initialize_database(db_path: str):
    """
    Inicializa la base de datos SQLite usando el esquema definido.
    """
    with open("infrastructure/baseDeDatos/esquema.sql", "r") as schema_file:
        schema = schema_file.read()

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.executescript(schema)  # Ejecuta todo el esquema SQL
        conn.commit()

if __name__ == "__main__":
    db_path = "database.db"  # Ruta de la base de datos
    initialize_database(db_path)
    print(f"Base de datos inicializada en {db_path}")
