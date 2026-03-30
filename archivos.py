import json

def guardar_clientes(clientes):
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo)
    print("Clientes guardados correctamente")

def cargar_clientes():
    clientes = []
    try:
        with open("clientes.json", "r") as archivo:
            clientes = json.load(archivo)
            print("Clientes cargados desde el archivo clientes.json")
    except FileNotFoundError:
        print("No se encontro el archivo clientes.json, se creara uno nuevo al guardar los clientes")
    return clientes
