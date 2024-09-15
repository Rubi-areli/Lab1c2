import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    # Función para validar y mostrar los datos ingresados en una nueva ventana
    def mostrar_resultado():
        cedula = entry_cedula.get()
        nombre = entry_nombre.get()

        # Validar que la cédula sea numérica y tenga al menos 8 caracteres
        if not cedula.isdigit() or len(cedula) < 8:
            messagebox.showerror("Error de Validación", "La cédula debe ser numérica y tener al menos 8 caracteres.")
            return
        
        # Validar que el nombre no esté vacío y contenga solo letras y espacios
        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error de Validación", "El nombre solo debe contener letras y espacios.")
            return

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

        # Mostrar el número de cédula y nombre completo en la nueva ventana
        resultado = tk.Label(nueva_ventana, text=f"Cédula: {cedula}\nNombre: {nombre}", font=("Arial", 16), justify="center")
        resultado.pack(expand=True, pady=20)

    # Crear ventana principal
    root = tk.Tk()
    root.title("Ingresar Cédula y Nombre")

    # Tamaño de la ventana principal
    ancho_ventana = 600
    alto_ventana = 400
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    # Etiqueta y campo de entrada para el número de cédula
    label_cedula = tk.Label(root, text="Ingrese su número de cédula:")
    label_cedula.pack(pady=20)
    entry_cedula = tk.Entry(root, font=("Arial", 14))
    entry_cedula.pack(pady=10)

    # Etiqueta y campo de entrada para el nombre completo
    label_nombre = tk.Label(root, text="Ingrese su nombre completo:")
    label_nombre.pack(pady=20)
    entry_nombre = tk.Entry(root, font=("Arial", 14))
    entry_nombre.pack(pady=10)

    # Botón para mostrar los datos ingresados
    boton_mostrar = tk.Button(root, text="Mostrar Datos", command=mostrar_resultado, font=("Arial", 14))
    boton_mostrar.pack(pady=20)

    # Ejecutar el loop de la ventana
    root.mainloop()

mostrar_datos()


#Nestor
