import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("mi_base_de_datos.db")
cursor = conn.cursor()

# Creación de la tabla Clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        clave TEXT PRIMARY KEY,
        nombre TEXT,
        direccion TEXT,
        correo_electronico TEXT,
        telefono TEXT
    )
''')

# Creación de la tabla Menú
cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu (
        clave TEXT PRIMARY KEY,
        nombre TEXT,
        precio REAL
    )
''')

# Creación de la tabla Pedido
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedido (
        duracion TEXT,
        pedido_id INTEGER PRIMARY KEY,
        cliente TEXT,
        producto TEXT,
        precio REAL
    )
''')

conn.commit()
conn.close()