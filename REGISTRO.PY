import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QComboBox, QSpinBox, QPushButton, QDialog, QMessageBox
from PyQt5.QtCore import Qt

class RegistroEvento(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Registro de Evento")
        self.setGeometry(0, 0, 500, 400)  # Tamaño más grande

        # Centrar la ventana en la pantalla
        self.centrar_ventana()

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta para seleccionar el género
        self.label_genero = QLabel("Seleccione su género:")
        layout.addWidget(self.label_genero)

        # Botones de radio para seleccionar el género
        self.radio_masculino = QRadioButton("Masculino")
        self.radio_femenino = QRadioButton("Femenino")
        layout.addWidget(self.radio_masculino)
        layout.addWidget(self.radio_femenino)

        # Etiqueta para seleccionar el país
        self.label_pais = QLabel("Seleccione su país:")
        layout.addWidget(self.label_pais)

        # ComboBox para seleccionar el país
        self.combobox_pais = QComboBox()
        self.combobox_pais.addItems(["El Salvador", "Guatemala", "Honduras", "México", "Costa Rica"])
        layout.addWidget(self.combobox_pais)

        # Etiqueta para seleccionar la edad
        self.label_edad = QLabel("Seleccione su edad:")
        layout.addWidget(self.label_edad)

        # SpinBox para seleccionar la edad
        self.spinbox_edad = QSpinBox()
        self.spinbox_edad.setRange(0, 120)  # Rango de edad de 0 a 120 años
        layout.addWidget(self.spinbox_edad)

        # Botón para registrar los datos
        self.boton_registrar = QPushButton("Registrar")
        self.boton_registrar.clicked.connect(self.validar_datos)
        layout.addWidget(self.boton_registrar)

        # Establecer el layout
        self.setLayout(layout)

    def centrar_ventana(self):
        # Obtener el tamaño de la pantalla
        pantalla = self.frameGeometry()
        centro_pantalla = QApplication.desktop().availableGeometry().center()
        pantalla.moveCenter(centro_pantalla)
        self.move(pantalla.topLeft())

    def validar_datos(self):
        # Validar que se haya seleccionado un género
        if not self.radio_masculino.isChecked() and not self.radio_femenino.isChecked():
            QMessageBox.warning(self, "Error de Validación", "Debe seleccionar un género.")
            return

        # Validar que la edad sea mayor que 0
        if self.spinbox_edad.value() == 0:
            QMessageBox.warning(self, "Error de Validación", "Debe seleccionar una edad mayor que 0.")
            return

        # Si todos los datos son válidos, mostrar los datos en la ventana
        self.mostrar_datos_en_ventana()

    def mostrar_datos_en_ventana(self):
        # Obtener los datos seleccionados
        genero = "Masculino" if self.radio_masculino.isChecked() else "Femenino"
        pais = self.combobox_pais.currentText()
        edad = self.spinbox_edad.value()

        # Crear una ventana emergente más grande (QDialog)
        dialogo = QDialog(self)
        dialogo.setWindowTitle("Datos Registrados")

        # Tamaño más grande de la ventana emergente
        ancho_ventana = 400
        alto_ventana = 300
        dialogo.resize(ancho_ventana, alto_ventana)

        # Centrar la ventana de diálogo
        pantalla_dialogo = dialogo.frameGeometry()
        centro_pantalla = QApplication.desktop().availableGeometry().center()
        pantalla_dialogo.moveCenter(centro_pantalla)
        dialogo.move(pantalla_dialogo.topLeft())

        # Crear layout para la nueva ventana
        layout_dialogo = QVBoxLayout()

        # Etiqueta para mostrar los datos centrados
        datos = QLabel(f"Género: {genero}\nPaís: {pais}\nEdad: {edad} años")
        datos.setAlignment(Qt.AlignCenter)  # Alinear al centro
        layout_dialogo.addWidget(datos)

        # Botón para cerrar la ventana
        boton_cerrar = QPushButton("Cerrar")
        boton_cerrar.clicked.connect(dialogo.accept)
        layout_dialogo.addWidget(boton_cerrar, alignment=Qt.AlignCenter)

        dialogo.setLayout(layout_dialogo)
        dialogo.exec_()  # Mostrar la ventana de diálogo


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear la ventana principal
    ventana = RegistroEvento()
    ventana.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())
