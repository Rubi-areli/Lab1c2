import tkinter as tk
from tkinter import messagebox

def ingresar_datos():
    # Función para mostrar los datos ingresados en una nueva ventana
    def mostrar_resultado():
        try:
            # Recoger los datos de las entradas
            nombre = entry_nombre.get()
            edad = int(entry_edad.get())  # Convertir edad a entero
            direccion = entry_direccion.get()
            telefono = entry_telefono.get()
            email = entry_email.get()
            ciudad = entry_ciudad.get()
            pais = entry_pais.get()
            ocupacion = entry_ocupacion.get()
            estado_civil = entry_estado_civil.get()
            genero = entry_genero.get()

            # Crear una nueva ventana para mostrar los resultados
            nueva_ventana = tk.Toplevel(root)
            nueva_ventana.title("Datos de la Persona Ingresados")

            # Tamaño de la nueva ventana
            ancho_ventana = 500
            alto_ventana = 400
            ancho_pantalla = nueva_ventana.winfo_screenwidth()
            alto_pantalla = nueva_ventana.winfo_screenheight()
            x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
            y_pos = (alto_pantalla // 2) - (alto_ventana // 2)

            nueva_ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

            # Mostrar los datos ingresados en la nueva ventana
            resultado = tk.Label(nueva_ventana, text=f"Nombre: {nombre}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\n"
                                                     f"Email: {email}\nCiudad: {ciudad}\nPaís: {pais}\nOcupación: {ocupacion}\n"
                                                     f"Estado Civil: {estado_civil}\nGénero: {genero}",
                                 font=("Arial", 14), justify="left")
            resultado.pack(expand=True, pady=20)
        except ValueError:
            messagebox.showerror("Error de Validación", "Por favor, ingrese datos válidos para todos los campos.")

    # Función para cambiar el foco al siguiente widget
    def mover_foco(event, siguiente_entry):
        siguiente_entry.focus()

    # Crear ventana principal
    root = tk.Tk()
    root.title("Ingresar 10 Datos de una Persona")

    # Tamaño de la ventana principal
    ancho_ventana = 700
    alto_ventana = 800
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    # Entrada para cada uno de los 10 datos
    label_nombre = tk.Label(root, text="Nombre:")
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(root, font=("Arial", 14), width=40)
    entry_nombre.pack(pady=5)

    label_edad = tk.Label(root, text="Edad:")
    label_edad.pack(pady=5)
    entry_edad = tk.Entry(root, font=("Arial", 14), width=40)
    entry_edad.pack(pady=5)

    label_direccion = tk.Label(root, text="Dirección:")
    label_direccion.pack(pady=5)
    entry_direccion = tk.Entry(root, font=("Arial", 14), width=40)
    entry_direccion.pack(pady=5)

    label_telefono = tk.Label(root, text="Teléfono:")
    label_telefono.pack(pady=5)
    entry_telefono = tk.Entry(root, font=("Arial", 14), width=40)
    entry_telefono.pack(pady=5)

    label_email = tk.Label(root, text="Email:")
    label_email.pack(pady=5)
    entry_email = tk.Entry(root, font=("Arial", 14), width=40)
    entry_email.pack(pady=5)

    label_ciudad = tk.Label(root, text="Ciudad:")
    label_ciudad.pack(pady=5)
    entry_ciudad = tk.Entry(root, font=("Arial", 14), width=40)
    entry_ciudad.pack(pady=5)

    label_pais = tk.Label(root, text="País:")
    label_pais.pack(pady=5)
    entry_pais = tk.Entry(root, font=("Arial", 14), width=40)
    entry_pais.pack(pady=5)

    label_ocupacion = tk.Label(root, text="Ocupación:")
    label_ocupacion.pack(pady=5)
    entry_ocupacion = tk.Entry(root, font=("Arial", 14), width=40)
    entry_ocupacion.pack(pady=5)

    label_estado_civil = tk.Label(root, text="Estado Civil:")
    label_estado_civil.pack(pady=5)
    entry_estado_civil = tk.Entry(root, font=("Arial", 14), width=40)
    entry_estado_civil.pack(pady=5)

    label_genero = tk.Label(root, text="Género:")
    label_genero.pack(pady=5)
    entry_genero = tk.Entry(root, font=("Arial", 14), width=40)
    entry_genero.pack(pady=5)

    # Asignar el evento <Return> a cada entrada para moverse a la siguiente
    entry_nombre.bind("<Return>", lambda event: mover_foco(event, entry_edad))
    entry_edad.bind("<Return>", lambda event: mover_foco(event, entry_direccion))
    entry_direccion.bind("<Return>", lambda event: mover_foco(event, entry_telefono))
    entry_telefono.bind("<Return>", lambda event: mover_foco(event, entry_email))
    entry_email.bind("<Return>", lambda event: mover_foco(event, entry_ciudad))
    entry_ciudad.bind("<Return>", lambda event: mover_foco(event, entry_pais))
    entry_pais.bind("<Return>", lambda event: mover_foco(event, entry_ocupacion))
    entry_ocupacion.bind("<Return>", lambda event: mover_foco(event, entry_estado_civil))
    entry_estado_civil.bind("<Return>", lambda event: mover_foco(event, entry_genero))

    # Botón para mostrar los datos ingresados
    boton_mostrar = tk.Button(root, text="Mostrar Datos", command=mostrar_resultado, font=("Arial", 14))
    boton_mostrar.pack(pady=20)

    # Ejecutar el loop de la ventana
    root.mainloop()

ingresar_datos()

#Nestor
