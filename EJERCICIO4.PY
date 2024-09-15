import tkinter as tk
from tkinter import messagebox

def ingresar_mascotas():
    # Función para mostrar los datos ingresados en una nueva ventana
    def mostrar_resultado():
        try:
            # Datos para la mascota 1
            nombre1 = entry_nombre1.get()
            tipo1 = entry_tipo1.get()
            edad1 = int(entry_edad1.get())  # Convertir edad a entero

            # Datos para la mascota 2
            nombre2 = entry_nombre2.get()
            tipo2 = entry_tipo2.get()
            edad2 = int(entry_edad2.get())

            # Datos para la mascota 3
            nombre3 = entry_nombre3.get()
            tipo3 = entry_tipo3.get()
            edad3 = int(entry_edad3.get())

            # Crear una nueva ventana para mostrar los resultados
            nueva_ventana = tk.Toplevel(root)
            nueva_ventana.title("Datos de Mascotas Ingresados")

            # Tamaño de la nueva ventana
            ancho_ventana = 500
            alto_ventana = 300
            ancho_pantalla = nueva_ventana.winfo_screenwidth()
            alto_pantalla = nueva_ventana.winfo_screenheight()
            x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
            y_pos = (alto_pantalla // 2) - (alto_ventana // 2)

            nueva_ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

            # Mostrar los datos de las tres mascotas en la nueva ventana
            resultado = tk.Label(nueva_ventana, text=f"Mascota 1:\nNombre: {nombre1}, Tipo: {tipo1}, Edad: {edad1} años\n\n"
                                                     f"Mascota 2:\nNombre: {nombre2}, Tipo: {tipo2}, Edad: {edad2} años\n\n"
                                                     f"Mascota 3:\nNombre: {nombre3}, Tipo: {tipo3}, Edad: {edad3} años",
                                 font=("Arial", 14), justify="center")
            resultado.pack(expand=True, pady=20)
        except ValueError:
            messagebox.showerror("Error de Validación", "Por favor, ingrese datos válidos para todas las mascotas.")

    # Función para limpiar texto cuando se enfoca una entrada
    def limpiar_entrada(event, entry):
        entry.delete(0, tk.END)

    # Crear ventana principal
    root = tk.Tk()
    root.title("Ingresar Datos de Mascotas")

    # Tamaño de la ventana principal
    ancho_ventana = 600
    alto_ventana = 500
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    # Entrada para Mascota 1
    label_mascota1 = tk.Label(root, text="Mascota 1")
    label_mascota1.pack(pady=10)
    entry_nombre1 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_nombre1.insert(0, "Nombre")
    entry_nombre1.pack(pady=5)
    entry_nombre1.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_nombre1))

    entry_tipo1 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_tipo1.insert(0, "Tipo de mascota (ej. Perro, Gato)")
    entry_tipo1.pack(pady=5)
    entry_tipo1.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_tipo1))

    entry_edad1 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_edad1.insert(0, "Edad")
    entry_edad1.pack(pady=5)
    entry_edad1.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_edad1))

    # Entrada para Mascota 2
    label_mascota2 = tk.Label(root, text="Mascota 2")
    label_mascota2.pack(pady=10)
    entry_nombre2 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_nombre2.insert(0, "Nombre")
    entry_nombre2.pack(pady=5)
    entry_nombre2.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_nombre2))

    entry_tipo2 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_tipo2.insert(0, "Tipo de mascota (ej. Perro, Gato)")
    entry_tipo2.pack(pady=5)
    entry_tipo2.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_tipo2))

    entry_edad2 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_edad2.insert(0, "Edad")
    entry_edad2.pack(pady=5)
    entry_edad2.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_edad2))

    # Entrada para Mascota 3
    label_mascota3 = tk.Label(root, text="Mascota 3")
    label_mascota3.pack(pady=10)
    entry_nombre3 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_nombre3.insert(0, "Nombre")
    entry_nombre3.pack(pady=5)
    entry_nombre3.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_nombre3))

    entry_tipo3 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_tipo3.insert(0, "Tipo de mascota (ej. Perro, Gato)")
    entry_tipo3.pack(pady=5)
    entry_tipo3.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_tipo3))

    entry_edad3 = tk.Entry(root, font=("Arial", 14), width=30)
    entry_edad3.insert(0, "Edad")
    entry_edad3.pack(pady=5)
    entry_edad3.bind("<FocusIn>", lambda event: limpiar_entrada(event, entry_edad3))

    # Botón para mostrar los datos ingresados
    boton_mostrar = tk.Button(root, text="Mostrar Datos", command=mostrar_resultado, font=("Arial", 14))
    boton_mostrar.pack(pady=20)

    # Ejecutar el loop de la ventana
    root.mainloop()

ingresar_mascotas()
