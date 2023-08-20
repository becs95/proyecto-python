import sqlite3

class ManejadorClientes:
    # Definición de la clase ManejadorClientes con funciones de agregar, eliminar, actualizar

    def agregar_cliente(self, cliente):
        # Agregar el cliente a la base de datos
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes VALUES (clave,nombre,direccion,correo,telefono)",
            (cliente.clave, cliente.nombre, cliente.direccion, cliente.correo_electronico, cliente.telefono))
        conn.commit()
        conn.close()

    def eliminar_cliente(self, clave):
        # Eliminar el cliente de la base de datos
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE clave=?", (clave,))
        conn.commit()
        conn.close()

    def actualizar_cliente(self, cliente):
        # Actualizar los datos del cliente en la base de datos
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET nombre=?, direccion=?, correo_electronico=?, telefono=? WHERE clave=?",
            (cliente.nombre, cliente.direccion, cliente.correo_electronico, cliente.telefono, cliente.clave))
        conn.commit()
        conn.close()