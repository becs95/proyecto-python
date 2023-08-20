

#rebeca soberanis trujillo 
#proyecto de python 

#creamos la funcion para imprimir 

def imprimir_menu():
    print("Menú:")
    print("a. Pedidos")
    print("b. Clientes")
    print("c. Menú")
    print("d. Salir")

def seleccionar_opcion():
    opcion = input("Selecciona una opción (a/b/c/d): ").lower()
    return opcion

def ejecutar_opcion(opcion):
    if opcion == 'a':
        print("Has seleccionado Pedidos.")
    elif opcion == 'b'== ManejadorPedidos:
        print("Has seleccionado Clientes.",ManejadorPedidos)
        
    elif opcion == 'c':
        print("Has seleccionado Menú.")
    elif opcion == 'd':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

def main():
    manejador_clientes = manejador_clientes()
    manejador_menu = manejador_menu()
    manejador_pedidos = manejador_pedidos()

def ManejadorPedidos():
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))
    unidades = int(input("Ingrese la cantidad de unidades: "))

    costo_total = precio_producto * unidades

    print("Simulación del pedido:")
    print(f"Producto: {nombre_producto}")
    print(f"Precio unitario: ${precio_producto:.2f}")
    print(f"Cantidad de unidades: {unidades}")
    print(f"Costo total: ${costo_total:.2f}")


# hacemos el modulo de clientes 

class Cliente:
    def __init__(self, clave, nombre, direccion, correo_electronico, telefono):
        self.clave = clave
        self.nombre = nombre
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.telefono = telefono

def agregar_cliente(clientes, cliente):
    clientes[cliente.clave] = cliente

def buscar_cliente(clientes, clave):
    return clientes.get(clave)

def mostrar_clientes(clientes):
    print("Lista de clientes:")
    for clave, cliente in clientes.items():
        print(f"Clave: {cliente.clave}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Dirección: {cliente.direccion}")
        print(f"Correo electrónico: {cliente.correo_electronico}")
        print(f"Teléfono: {cliente.telefono}")
        print("=" * 30)

def eliminar_cliente(clientes, clave):
    if clave in clientes:
        del clientes[clave]
        print(f"Cliente con clave {clave} eliminado.")
    else:
        print(f"No se encontró ningún cliente con clave {clave}.")

    # Diccionario para almacenar clientes (clave: cliente)
    clientes_data = {}

    # Crear clientes de ejemplo
    cliente1 = Cliente("c1", "Cliente 1", "Dirección 1", "correo1@example.com", "123456789")
    cliente2 = Cliente("c2", "Cliente 2", "Dirección 2", "correo2@example.com", "987654321")

    # Agregar clientes al diccionario
    agregar_cliente(clientes_data, cliente1)
    agregar_cliente(clientes_data, cliente2)

    # Mostrar la lista de clientes
    mostrar_clientes(clientes_data)

    # Buscar y mostrar un cliente por su clave
    clave_buscar = "c1"
    cliente_encontrado = buscar_cliente(clientes_data, clave_buscar)
    if cliente_encontrado:
        print("Cliente encontrado:")
        print(f"Clave: {cliente_encontrado.clave}")
        print(f"Nombre: {cliente_encontrado.nombre}")
    else:
        print(f"No se encontró ningún cliente con clave {clave_buscar}.")

    # Eliminar un cliente por su clave
    clave_eliminar = "c2"
    eliminar_cliente(clientes_data, clave_eliminar)

    # Mostrar la lista de clientes actualizada
    mostrar_clientes(clientes_data)
    

# hacemos el modulo de menú

class Producto:
    def __init__(self, clave, nombre, precio):
        self.clave = clave
        self.nombre = nombre
        self.precio = precio

class ManejadorMenu:
    def __init__(self):
        self.menu = {}

    def agregar_producto(self, producto):
        self.menu[producto.clave] = producto

    def eliminar_producto(self, clave):
        if clave in self.menu:
            del self.menu[clave]
            print(f"Producto con clave {clave} eliminado.")
        else:
            print(f"No se encontró ningún producto con clave {clave}.")

    def actualizar_producto(self, clave, nombre, precio):
        if clave in self.menu:
            producto = self.menu[clave]
            producto.nombre = nombre
            producto.precio = precio
            print(f"Producto con clave {clave} actualizado.")
        else:
            print(f"No se encontró ningún producto con clave {clave}.")

    def mostrar_menu(self):
        print("Menú:")
        for clave, producto in self.menu.items():
            print(f"Clave: {producto.clave}")
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print("=" * 30)

#creamos el modulo pedido

class Pedido:
    def __init__(self, duracion, pedido_id, cliente, producto, precio):
        self.duracion = duracion
        self.pedido_id = pedido_id
        self.cliente = cliente
        self.producto = producto
        self.precio = precio

class ManejadorPedidos:
    def __init__(self):
        self.pedidos = {}
        self.pedido_id_counter = 1

    def crear_pedido(self, duracion, cliente, producto, precio):
        pedido_id = self.pedido_id_counter
        pedido = Pedido(duracion, pedido_id, cliente, producto, precio)
        self.pedidos[pedido_id] = pedido
        self.pedido_id_counter += 1
        return pedido_id

    def cancelar_pedido(self, pedido_id):
        if pedido_id in self.pedidos:
            del self.pedidos[pedido_id]
            print(f"Pedido {pedido_id} cancelado.")
        else:
            print(f"No se encontró ningún pedido con ID {pedido_id}.")

    def mostrar_pedidos(self):
        print("Lista de pedidos:")
        for pedido_id, pedido in self.pedidos.items():
            print(f"Duración: {pedido.duracion}")
            print(f"ID del pedido: {pedido.pedido_id}")
            print(f"Cliente: {pedido.cliente}")
            print(f"Producto: {pedido.producto}")
            print(f"Precio: {pedido.precio}")
            print("=" * 30)
    
    