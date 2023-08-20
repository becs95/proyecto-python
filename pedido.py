import sqlite3

class ManejadorPedidos:
    # Definición de la clase ManejadorPedidos con funciones de crear pedido, cancelar pedido

    def crear_pedido(self, duracion, cliente, producto, precio):
        # Consultar nombre de cliente y producto en la base de datos
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM clientes WHERE clave=?", (cliente,))
        cliente_nombre = cursor.fetchone()[0]
        cursor.execute("SELECT nombre FROM menu WHERE clave=?", (producto,))
        producto_nombre = cursor.fetchone()[0]
        conn.close()

        # Insertar el pedido en la base de datos
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedido (duracion, cliente, producto, precio) VALUES (?, ?, ?, ?)",
            (duracion, cliente_nombre, producto_nombre, precio))
        conn.commit()
        conn.close()

        # Simular impresión de ticket
        self.imprimir_ticket(cliente_nombre, producto_nombre, precio)

    def imprimir_ticket(self, cliente, producto, precio):
        with open("ticket.txt", "w") as f:
            f.write("Ticket de Pedido\n")
            f.write("=================\n")
            f.write(f"Cliente: {cliente}\n")
            f.write(f"Producto: {producto}\n")
            f.write(f"Precio: ${precio:.2f}\n")
            f.write("=================\n")
            f.write("¡Gracias por su pedido!")