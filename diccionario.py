import json
from color import exito, error, info, separador, input_color, AZUL, NEGRITA, RESET, AMARILLO

clientes = []
def crear_cliente(clientes, ID, Nombre, Edad, tipo_plan, Estado):
    cliente = {
        "ID": ID,
        "nombre": Nombre,
        "edad": Edad,
        "tipo_plan": tipo_plan,
        "estado": Estado
    }
    clientes.append(cliente)
    print(f"Cliente {Nombre} creado correctamente")

def json_clientes(clientes):
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo)
    for cliente in clientes:
        print(f"nombre: {cliente['nombre']}")
        print(f"edad: {cliente['edad']}")
        print(f"ID: {cliente['ID']}")
        print(f"tipo_plan: {cliente['tipo_plan']}")
        print(f"estado: {cliente['estado']}")
        print("------------------------")

def listar_clientes(cliente):
    if not cliente:
        error("Aun no hay clientes registrados")
        return
    print(f"{AZUL}{NEGRITA}Lista de clientes:{RESET}")
    for cliente in clientes:
        info(f"ID: {cliente['ID']} | Nombre: {cliente['nombre']} | Edad: {cliente['edad']} | tipo_plan: {cliente['tipo_plan']} | estado: {cliente['estado']}")
    separador()

def buscar_cliente(clientes, cliente_ID):
    for cliente in clientes:
        if cliente['ID'] == cliente_ID:
            info(f"Cliente encontrado:")
            info(f"ID: {cliente['ID']} | Nombre: {cliente['nombre']} | Edad: {cliente['edad']} | tipo_plan: {cliente['tipo_plan']} | estado: {cliente['estado']}")
            return
    error("Cliente no encontrado")

def actualizar_cliente(clientes, cliente_ID):
    for cliente in clientes:
        if cliente['ID'] == cliente_ID:
            nuevo_nombre = input_color("Ingrese el nuevo nombre del cliente: ", AMARILLO)
            nueva_edad = int(input_color("Ingrese la nueva edad del cliente: ", AMARILLO))
            cliente['nombre'] = nuevo_nombre
            cliente['edad'] = nueva_edad
            exito("Cliente actualizado correctamente")
            return
    error("Cliente no encontrado")

def eliminar_cliente(clientes, cliente_ID):
    for cliente in clientes:
        if cliente['ID'] == cliente_ID:
            clientes.remove(cliente)
            exito("Cliente eliminado correctamente")
            return
    error("Cliente no encontrado")

