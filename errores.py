
def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un numero valido")

def error_opcion():
    print("Opcion no valida, por favor elija una opcion del 1 al 6")


def tipo_plan():
    while True:
        try:
            tipo_plan = input("Ingrese el tipo de plan (mensual, trimenstral, anual): ").lower()
            if tipo_plan in ["mensual", "trimestral", "anual"]:
                return tipo_plan
            else:
                print("Tipo de plan no valido, por favor ingrese 'mensual', 'trimestral' o 'anual'")
        except ValueError:
            print("Error: debe ingresar un tipo de plan valido")