import tkinter as tk

def ingresar_clave():
    # Función para mostrar la clave ingresada
    def mostrar_clave():
        clave = entry_clave.get()
        if clave:
            resultado.config(text="Clave ingresada correctamente")
        else:
            resultado.config(text="Por favor, ingrese una clave")

    # Crear ventana principal
    root = tk.Tk()
    root.title("Ingresar Clave Secreta")

    # Tamaño de la ventana
    ancho_ventana = 400
    alto_ventana = 200
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    # Etiqueta para la clave
    label_clave = tk.Label(root, text="Ingrese su clave secreta:")
    label_clave.pack(pady=20)

    # Campo de entrada para la clave, con los caracteres ocultos
    entry_clave = tk.Entry(root, show="*", font=("Arial", 14))  # show="*" oculta los caracteres
    entry_clave.pack(pady=10)

    # Botón para confirmar la clave
    boton_confirmar = tk.Button(root, text="Confirmar Clave", command=mostrar_clave, font=("Arial", 14))
    boton_confirmar.pack(pady=20)

    # Etiqueta para mostrar si la clave fue ingresada correctamente
    resultado = tk.Label(root, text="", font=("Arial", 14), justify="center")
    resultado.pack(pady=20)

    # Ejecutar el loop de la ventana
    root.mainloop()

ingresar_clave()
