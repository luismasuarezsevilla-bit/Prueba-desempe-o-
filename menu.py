from diccionario import clientes, crear_cliente, listar_clientes, buscar_cliente, actualizar_cliente, eliminar_cliente
from archivos import guardar_clientes, cargar_clientes
from color import titulo, exito, error, info, menu_opcion, separador, input_color, AMARILLO, VERDE
# para definir el menu principal del programa
# se muestra el menu y se pide al ususario que elija una opcion hasta que elija salir
# se llama a las funciones correspondientes segun la opcion elegida
def menu():
    clientes_data = cargar_clientes()
    clientes.clear()
    clientes.extend(clientes_data)
    titulo("SISTEMA DE GESTIÓN DE CLIENTES")
# el while True hace que el menu muestre continuamente hasta que el usuario elija salir.
while True:
        print()
        menu_opcion("1", "Crear cliente")
        menu_opcion("2", "Listar clientes")
        menu_opcion("3", "Buscar cliente")
        menu_opcion("4", "Actualizar cliente")
        menu_opcion("5", "Eliminar cliente")
        menu_opcion("6", "Salir")
        separador()
        print()

        opcion = input("\u2192 Que opcion desea elegir: ")
        # se valida que la opcion sea un numero del 1 al 6, si no es asi se muestra un mensaje de error y se vuelve a mostrar el menu
        if opcion == "1":
            print()
            info("Bienvenido al formulario de registro")
            cliente_ID = int(input_color("\n  Ingrese su ID o CC: ", AMARILLO))
            
            cliente = input_color("  Ingrese su Nombre: ", AMARILLO)
        
            Edad = int(input_color("  Ingrese su edad: ", AMARILLO))
            
            tipo_plan = input_color("  Ingrese el tipo de plan (mensual, trimenstral, anual): ", AMARILLO).lower()
            # se valida que el tipo de plan sea mensual, trimestral o anual, si no es asi se muestra un mensaje de error y se vuelve a pedir el tipo de plan
            while tipo_plan not in ["mensual", "trimestral", "anual"]:
                error("Tipo de plan no valido, por favor ingrese 'mensual', 'trimestral' o 'anual'")
                tipo_plan = input_color("  Ingrese el tipo de plan (mensual, trimenstral, anual): ", AMARILLO).lower()

            Estado = input_color(" Ingrese el estado del cliente (activo, inactivo): ", AMARILLO)
            print(f"Estado: {Estado}")

            if Estado.isalpha() and Estado.lower() in ["activo", "inactivo"]:

                exito(f"Estado '{Estado}' registrado correctamente")

            else:
                error("Estado no valido, por favor ingrese 'activo' o 'inactivo'")
                continue

            # se llama a la funcion crear_cliente con los datos ingresados por el usuario
            # luego se guarda la lista de clientes en el archivo JSON y se muestra un mensaje de exito
            crear_cliente(clientes, cliente_ID, cliente, Edad, tipo_plan, Estado)
            guardar_clientes(clientes)
            exito("Cliente creado y guardado correctamente")

        elif opcion == "2":
            listar_clientes(clientes)

        elif opcion == "3":
            print()
            cliente_ID = int(input_color("Ingrese el ID del cliente que desea buscar: ", AMARILLO))
            buscar_cliente(clientes, cliente_ID)

        elif opcion == "4":
            print()
            cliente_ID = int(input_color("Ingrese el ID del cliente que desea actualizar: ", AMARILLO))
            actualizar_cliente(clientes, cliente_ID)
            guardar_clientes(clientes)
            exito("Cambios guardados en el archivo JSON")

        elif opcion == "5":
            print()
            cliente_ID = int(input_color("Ingrese el ID del cliente que desea eliminar: ", AMARILLO))
            eliminar_cliente(clientes, cliente_ID)
            guardar_clientes(clientes)
            exito("Cambios guardados en el archivo JSON")

        elif opcion == "6":
            exito("Gracias por usar el programa. ¡Hasta luego!")
            break

        else:
            error("Opcion no valida, por favor elija una opcion del 1 al 6")
            
menu()

