import tkinter as tk

def mostrar_datos():
    # Función para mostrar los datos ingresados en una nueva ventana
    def mostrar_resultado():
        nombre = entry_nombre.get()
        edad = entry_edad.get()

        if nombre and edad:
            try:
                # Convertir la edad a número para validar si es un número válido
                edad = int(edad)

                # Crear una nueva ventana para mostrar los resultados
                nueva_ventana = tk.Toplevel(root)
                nueva_ventana.title("Datos Ingresados")

                # Tamaño de la nueva ventana
                ancho_ventana = 400
                alto_ventana = 200
                ancho_pantalla = nueva_ventana.winfo_screenwidth()
                alto_pantalla = nueva_ventana.winfo_screenheight()
                x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
                y_pos = (alto_pantalla // 2) - (alto_ventana // 2)

                nueva_ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

                # Mostrar el nombre y edad en la nueva ventana
                resultado = tk.Label(nueva_ventana, text=f"Nombre: {nombre}\nEdad: {edad}", font=("Arial", 16), justify="center")
                resultado.pack(expand=True, pady=20)
            except ValueError:
                resultado.config(text="Error: La edad debe ser un número válido", justify="center")
        else:
            resultado.config(text="Por favor, ingrese todos los datos", justify="center")

    # Crear ventana principal
    root = tk.Tk()
    root.title("Ingresar Nombre y Edad")

    # Tamaño de la ventana principal
    ancho_ventana = 600
    alto_ventana = 400
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    # Etiqueta y campo de entrada para el nombre
    label_nombre = tk.Label(root, text="Ingrese su nombre:")
    label_nombre.pack(pady=20)
    entry_nombre = tk.Entry(root, font=("Arial", 14))
    entry_nombre.pack(pady=10)

    # Etiqueta y campo de entrada para la edad
    label_edad = tk.Label(root, text="Ingrese su edad:")
    label_edad.pack(pady=20)
    entry_edad = tk.Entry(root, font=("Arial", 14))
    entry_edad.pack(pady=10)

    # Botón para mostrar los datos ingresados
    boton_mostrar = tk.Button(root, text="Mostrar Datos", command=mostrar_resultado, font=("Arial", 14))
    boton_mostrar.pack(pady=20)

    # Ejecutar el loop de la ventana
    root.mainloop()

mostrar_datos()

