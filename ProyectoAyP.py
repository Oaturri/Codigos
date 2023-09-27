objetos = []

def registrar_usuario():
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    while edad < 18:
        print("Debes tener al menos 18 años para registrarte.")
        edad = int(input("Introduce tu edad: "))
    carnet_estudiantil = input("Introduce tu carnet estudiantil: ")

def publicar_objeto():
    nombre = input("Nombre del objeto: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    objetos.append({"nombre": nombre, "descripcion": descripcion, "precio": precio, "cantidad": cantidad})

def revisar_objetos():
    for i, obj in enumerate(objetos, 1):
        print(f"{i}. {obj['nombre']} - {obj['descripcion']} - Precio: {obj['precio']} - Cantidad: {obj['cantidad']}")

    opcion = int(input("Selecciona el número del objeto del cual deseas comprar o 0 para regresar: "))

    if opcion > 0 and opcion <= len(objetos):
        cantidad_a_quitar = int(input(f"¿Cuántas unidades del '{objetos[opcion-1]['nombre']}' deseas comprar? "))
        
        if cantidad_a_quitar <= objetos[opcion-1]['cantidad']:
            precio_total = cantidad_a_quitar * objetos[opcion-1]['precio']
            objetos[opcion-1]['cantidad'] -= cantidad_a_quitar

            if objetos[opcion-1]['cantidad'] <= 0:
                objetos.pop(opcion - 1)
                print("Objeto eliminado por falta de stock.")
            else:
                print(f"Quedan {objetos[opcion-1]['cantidad']} unidades.")
            
            print(f"Precio Total: {precio_total}")
        else:
            print("No hay suficiente stock para esa cantidad.")
    else:
        print("Opción no válida.")

def menu():
    registrar_usuario()
    while True:
        print("\nMenu:")
        print("1. Publicar objeto")
        print("2. Revisar objetos")
        print("3. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            publicar_objeto()
        elif opcion == 2:
            revisar_objetos()
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()