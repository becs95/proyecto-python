import sqlite3

class ManejadorMenu:
    # Definición de la clase ManejadorMenu con funciones de agregar, eliminar, actualizar

    def agregar_producto(self, producto):
        # Agregar el producto a la base de datos
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute(('clave','nombre', 'precio'),
        (producto.clave, producto.nombre, producto.precio))
        conn.commit()
        conn.close()

    def eliminar_producto(self, clave):
        # Eliminar el producto de la base de datos
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM menu WHERE clave=?", (clave,))
        conn.commit()
        conn.close()

    def actualizar_producto(self, producto):
        # Actualizar los datos del producto en la base de datos
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute(('UPDATE','clave','nombre', 'precio'),
            (producto.nombre, producto.precio, producto.clave))
        conn.commit()
        conn.close()
        