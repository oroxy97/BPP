from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

# Definimos la clase
class Window(QMainWindow):

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

        equation = self.label.text()

        try:

            ans = eval(equation)

            self.label.setText(str(ans))


        except:

            self.label.setText("Wrong Input")

    def action_suma(self):

        text = self.label.text()
        self.label.setText(text + " + ")

    def action_resta(self):

        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):

        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):

        text = self.label.text()
        self.label.setText(text + " * ")

    def action_punto(self):

        text = self.label.text()
        self.label.setText(text + ".")

    def b0(self):

        text = self.label.text()
        self.label.setText(text + "0")

    def b1(self):

        text = self.label.text()
        self.label.setText(text + "1")

    def b2(self):

        text = self.label.text()
        self.label.setText(text + "2")

    def b3(self):

        text = self.label.text()
        self.label.setText(text + "3")

    def b4(self):

        text = self.label.text()
        self.label.setText(text + "4")

    def b5(self):

        text = self.label.text()
        self.label.setText(text + "5")

    def b6(self):

        text = self.label.text()
        self.label.setText(text + "6")

    def b7(self):

        text = self.label.text()
        self.label.setText(text + "7")

    def b8(self):

        text = self.label.text()
        self.label.setText(text + "8")

    def b9(self):

        text = self.label.text()
        self.label.setText(text + "9")

    def action_limpiar(self):

        self.label.setText("")

    def action_borrar(self):

        text = self.label.text()

        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec_())
