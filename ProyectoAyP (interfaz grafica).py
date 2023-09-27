import tkinter as tk
from tkinter import simpledialog, messagebox

objetos = []

def registrar_usuario():
    nombre = simpledialog.askstring("Registro", "Introduce tu nombre:")
    edad = simpledialog.askinteger("Registro", "Introduce tu edad:")
    while edad < 18:
        messagebox.showerror("Error", "Debes tener al menos 18 años para registrarte.")
        edad = simpledialog.askinteger("Registro", "Introduce tu edad:")
    carnet_estudiantil = simpledialog.askstring("Registro", "Introduce tu carnet estudiantil:")

def publicar_objeto():
    nombre = simpledialog.askstring("Publicar Objeto", "Nombre del objeto:")
    descripcion = simpledialog.askstring("Publicar Objeto", "Descripción:")
    precio = simpledialog.askfloat("Publicar Objeto", "Precio:")
    cantidad = simpledialog.askinteger("Publicar Objeto", "Cantidad:")
    objetos.append({"nombre": nombre, "descripcion": descripcion, "precio": precio, "cantidad": cantidad})

def revisar_objetos():
    lista_objetos = "\n".join([f"{i+1}. {obj['nombre']} - {obj['descripcion']} - Precio: {obj['precio']} - Cantidad: {obj['cantidad']}" for i, obj in enumerate(objetos)])
    opcion = simpledialog.askinteger("Revisar Objetos", f"{lista_objetos}\n\nSelecciona el número del objeto del cual deseas comprar o 0 para regresar:")
    
    if opcion > 0 and opcion <= len(objetos):
        cantidad_a_quitar = simpledialog.askinteger("Comprar Objeto", f"¿Cuántas unidades del '{objetos[opcion-1]['nombre']}' deseas comprar?")
        
        if cantidad_a_quitar <= objetos[opcion-1]['cantidad']:
            precio_total = cantidad_a_quitar * objetos[opcion-1]['precio']
            objetos[opcion-1]['cantidad'] -= cantidad_a_quitar

            if objetos[opcion-1]['cantidad'] <= 0:
                objetos.pop(opcion - 1)
                messagebox.showinfo("Información", "Objeto eliminado por falta de stock.")
            else:
                messagebox.showinfo("Información", f"Quedan {objetos[opcion-1]['cantidad']} unidades.")
            
            messagebox.showinfo("Información", f"Precio Total: {precio_total}")
        else:
            messagebox.showerror("Error", "No hay suficiente stock para esa cantidad.")
    else:
        messagebox.showerror("Error", "Opción no válida.")

def menu():
    registrar_usuario()
    while True:
        opcion = simpledialog.askinteger("Menú", "1. Publicar objeto\n2. Revisar objetos\n3. Salir\n\nElige una opción:")
        if opcion == 1:
            publicar_objeto()
        elif opcion == 2:
            revisar_objetos()
        elif opcion == 3:
            messagebox.showinfo("Información", "¡Hasta luego!")
            break
        else:
            messagebox.showerror("Error", "Opción no válida.")

root = tk.Tk()
root.withdraw()  # Oculta la ventana principal de tkinter
menu()
