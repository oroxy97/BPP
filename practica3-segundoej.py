from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# Definimos la clase
class Window(QMainWindow):
    """
    Window:
    Atributos:
    ----------
    __init__:
        setWindowTitle:
            Será el nombre de nuestra aplicacion cuando la ejecutemos
        setGeometry:
            Será las dimensiones de nuestra aplicacion
        UiComponents:
            Definimos la opción para desarrollar GUI(Graphical User Interface) que en nuestro caso es PyQt5
        Show:
            Mostramos el programa
    UiComponents
        QLabel:
            Se utiliza para mostrar texto o una imagen
        setGeometry:
            Definimos la geometria, el tamaño dentro del espacio de nuestra app de la etiqueta
        setWordWrap:
            Ajustamos las lineas a lo largo de los límites de las palabras con esta propiedad
        setStyleSheet:
            Personalización de los colores de primer plano y de fondo
        setAlignment:
            Se utiliza para establecer la alineación de ls widgets
        setFont:
            Se utiliza para elegir la fuente y el tamaño
         BUTTONS:
         -------
         button1:
            Creamos el boton con el numero 1 y le asignamos los metodos y atributos de la funcion b1.
        button2:
            Creamos el boton con el numero 2 y le asignamos los metodos y atributos de la funcion b2.
        button3:
            Creamos el boton con el numero 3 y le asignamos los metodos y atributos de la funcion b3.
        button4:
            Creamos el boton con el numero 4 y le asignamos los metodos y atributos de la funcion b4.
        button5:
            Creamos el boton con el numero 5 y le asignamos los metodos y atributos de la funcion b5.
        button6:
            Creamos el boton con el numero 6 y le asignamos los metodos y atributos de la funcion b6.
        button7:
            Creamos el boton con el numero 7 y le asignamos los metodos y atributos de la funcion b7.
        button8:
            Creamos el boton con el numero 8 y le asignamos los metodos y atributos de la funcion b8.
        button9:
            Creamos el boton con el numero 9 y le asignamos los metodos y atributos de la funcion b9.
        button0:
            Creamos el boton con el numero 0 y le asignamos los metodos y atributos de la funcion b0.
        button_igual:
            Creamos el boton con el simbolo igual y le asignamos lo metodos y atributos de la funcion action_igual.
        button_suma:
            Creamos el boton con el simbolo suma y le asignamos los metodos y atributos de la funcion action_suma.
        button_resta:
            Creamos el boton con el simbolo resta y le asignamos los metodos y atributos de la funcion action_resta.
        button_mul:
            Creamos el boton con el simbolo de multiplicar y le asignamos los metodos y atributos de la funcion action_mul.
        button_div:
            Creamos el boton con el simbolo de dividir y le asignamos los metodos y atributos de la funcion action_div.
        button_punto:
            Creamos el boton con el simbolo de un punto y le asignamos los metodos y atributos de la funcion action_punto.
        button_limpiar:
            Creamos el boton con el simbolo cl y le asignamos los metodos y atributos de la funcion action_limpiar.
        button_borrar:
            Creamos el boton con el simbolo del y le asignamos los metodos y atributos con la funcion action_borrar.
    METODOS:
    -------
    Definimos las funciones:
        action_igual:
            Nos da el resultado entre los distintos operandos que hayamos usado.
        action_suma:
            Realiza la suma entre dos operandos.
        action_resta:
            Realiza la resta entre dos operandos.
        action_div:
            Realiza la division entre dos operandos.
        action_mul:
            Realiza la multiplicacion entre dos operandos.
        action_punto:
            Lo usamos para convertir un número con decimales.
        b0:
            Definimos la funcion para el boton 0.
        b1:
            Definimos la funcion para el boton 1.
        b2:
            Definimos la funcion para el boton 2.
        b3:
            Definimos la funcion para el boton 3.
        b4:
            Definimos la funcion para el boton 4.
        b5:
            Definimos la funcion para el boton 5.
        b6:
            Definimos la funcion para el boton 6.
        b7:
            Definimos la funcion para el boton 7.
        b8:
            Definimos la funcion para el boton 8.
        b9:
            Definimos la funcion para el boton 9.
        action_limpiar:
            Definimos la funcion limpiar para borrar la pantalla.
        action_borrar:
            Definimos la funcion para borrar todos lo procesos.


    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python")

        self.setGeometry(100,100,350,360)

        self.UiComponents()

        self.show()


    def UiComponents(self):

        self.label = QLabel(self)

        self.label.setGeometry(5, 5, 350, 70)

        self.label.setWordWrap(True)

        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")

        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 15))

# Botones
        button1 = QPushButton("1", self)
        button1.setGeometry(5, 150, 80, 40)
        button1.clicked.connect(self.b1)

        button2 = QPushButton("2", self)
        button2.setGeometry(95, 150, 80, 40)
        button2.clicked.connect(self.b2)

        button3 = QPushButton("3", self)
        button3.setGeometry(185, 150, 80, 40)
        button3.clicked.connect(self.b3)

        button4 = QPushButton("4", self)
        button4.setGeometry(5, 200, 80, 40)
        button4.clicked.connect(self.b4)

        button5 = QPushButton("5", self)
        button5.setGeometry(95, 200, 80, 40)
        button5.clicked.connect(self.b5)

        button6 = QPushButton("6", self)
        button6.setGeometry(185, 200, 80, 40)
        button6.clicked.connect(self.b6)

        button7 = QPushButton("7", self)
        button7.setGeometry(5, 250, 80, 40)
        button7.clicked.connect(self.b7)

        button8 = QPushButton("8", self)
        button8.setGeometry(95, 250, 80, 40)
        button8.clicked.connect(self.b8)

        button9 = QPushButton("9", self)
        button9.setGeometry(185, 250, 80, 40)
        button9.clicked.connect(self.b9)

        button0 = QPushButton("0", self)
        button0.setGeometry(5, 300, 80, 40)
        button0.clicked.connect(self.b0)

        button_igual = QPushButton("=", self)
        button_igual.setGeometry(275, 300, 80, 40)
        button_igual.clicked.connect(self.action_igual)
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        button_igual.setGraphicsEffect(c_effect)

        button_suma = QPushButton("+", self)
        button_suma.setGeometry(275, 250, 80, 40)
        button_suma.clicked.connect(self.action_suma)

        button_resta = QPushButton("-", self)
        button_resta.setGeometry(275, 200, 80, 40)
        button_resta.clicked.connect(self.action_resta)

        button_mul = QPushButton("*", self)
        button_mul.setGeometry(275, 150, 80, 40)
        button_mul.clicked.connect(self.action_mul)

        button_div = QPushButton("/", self)
        button_div.setGeometry(185, 300, 80, 40)
        button_div.clicked.connect(self.action_div)

        button_punto = QPushButton(".", self)
        button_punto.setGeometry(95, 300, 80, 40)
        button_punto.clicked.connect(self.action_punto)

        button_limpiar = QPushButton("cl", self)
        button_limpiar.setGeometry(5, 100, 200, 40)
        button_limpiar.clicked.connect(self.action_limpiar)

        button_borrar = QPushButton("del", self)
        button_borrar.setGeometry(210, 100, 145, 40)
        button_borrar.clicked.connect(self.action_borrar)

# Definimos las funciones
    def action_igual(self):
        """
        Nos da el resultado entre los distintos operandos que hayamos usado.
        """
        equation = self.label.text()

        try:

            ans = eval(equation)

            self.label.setText(str(ans))


        except:

            self.label.setText("Wrong Input")


    def action_suma(self):
        """
        Realiza la suma entre dos operandos.
        """
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_resta(self):
        """
        Realiza la resta entre dos operandos.
        """

        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        """
        Realiza la division entre dos operandos.
        """
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        """
        Realiza la multiplicacion entre dos operandos.
        """
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_punto(self):
        """
        Lo usamos para convertir un número con decimales.
        """

        text = self.label.text()
        self.label.setText(text + ".")

    def b0(self):
        """
        Definimos la funcion para el boton 0.
        """

        text = self.label.text()
        self.label.setText(text + "0")

    def b1(self):
        """
        Definimos la funcion para el boton 1.
        """

        text = self.label.text()
        self.label.setText(text + "1")

    def b2(self):
        """
        Definimos la funcion para el boton 2.
        """

        text = self.label.text()
        self.label.setText(text + "2")

    def b3(self):
         """
         Definimos la funcion para el boton 3.
         """

        text = self.label.text()
        self.label.setText(text + "3")

    def b4(self):
        """
        Definimos la funcion para el boton 4.
        """

        text = self.label.text()
        self.label.setText(text + "4")

    def b5(self):
        """
        Definimos la funcion para el boton 5.
        """

        text = self.label.text()
        self.label.setText(text + "5")

    def b6(self):
        """
        Definimos la funcion para el boton 6.
        """
        text = self.label.text()
        self.label.setText(text + "6")

    def b7(self):
        """
        Definimos la funcion para el boton 7.
        """

        text = self.label.text()
        self.label.setText(text + "7")

    def b8(self):
        """
        Definimos la funcion para el boton 8.
        """

        text = self.label.text()
        self.label.setText(text + "8")

    def b9(self):
        """
        Definimos la funcion para el boton 9.
        """
        text = self.label.text()
        self.label.setText(text + "9")

    def action_limpiar(self):
        """
        Definimos la funcion limpiar para borrar la pantalla.
        """
        self.label.setText("")

    def action_borrar(self):
        """
        Definimos la funcion para borrar todos lo procesos.
        """
        text = self.label.text()

        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec_())
