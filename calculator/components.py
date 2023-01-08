from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QGridLayout
from tools.validators import isFloat

class Display(QLabel):
    def __init__(self, value=0):
        super().__init__()
        self.value = value

    @property
    def value(self):
        return float(self.text())

    @value.setter
    def value(self, text):
        if isFloat(text):
            self.setText(f"{text}")
        else:
            raise ValueError(f"{text} debe ser numérico")

class CalcButton(QPushButton):
    def __init__(self, text, command=lambda x: print(x)):
        super().__init__(f"{text}")
        self.connect(command)
        self.setFixedSize(66, 60)

    def setColor(self, color):
        self.setStyleSheet(f"background-color: {color}")

    def connect(self, command):
        try:
            self.clicked.disconnect()
        except TypeError:
            pass
        self.clicked.connect(lambda: command(self.text()))



class KeyPad(QWidget):
    def __init__(self, cols=3, lines=3):
        super().__init__()
        self.layout = self.__createLayout()
        self.buttons = [[None for j in range(cols)] for i in range(lines)]
        self.cols = cols
        self.lines = lines

    def __createLayout(self):
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setLayout(layout)
        return layout
    
    def addWidget(self, ctrl, col, line):
        if col >= self.cols or col < 0:
            raise ValueError(f"Choose a column between 0 and {self.cols-1}")
        if line >= self.lines or line < 0:
            raise ValueError(f"Choose a line between 0 and {self.lines-1}")

        if isinstance(ctrl, tuple) or isinstance(ctrl, list):
            btn = CalcButton(ctrl[0])
            btn.setColor(ctrl[1])
        else:
            btn = CalcButton(ctrl)
        self.layout.addWidget(btn, line, col)

        self.buttons[line][col] = btn

    def connect(self, col, line, command):
        self.buttons[line][col].connect(command)


class Calculator(QWidget):
    buttons = (
                (("C", "#626065"), ("+/-", "#626065"), ("%", "#626065"), ("÷", "#FF9E0B")),
                ("7", "8", "9", ("x", "#FF9E0B")),
                ("4", "5", "6", ("-", "#FF9E0B")),
                ("1", "2", "3", ("+", "#FF9E0B")),
                ("↩︎", "0", ".", ("=", "#FF9E0B"))
              )
    def operation(self, op):
        base = self.display.text()
        if op in tuple("0123456789"):
            if base == "0" or (self.operador and not self.op2):
                pass
            else:
                op = base + op
        elif op == ".":
            if "." not in base:
                op = base + op
            else:
                op = base
        elif op == "↩︎":
            op = self.display.text()[:-1] or "0"
        elif op == "C":
            op = "0"
            self.operador = self.op1 = self.op2 = None
        elif op == "+/-":
            if base == "0":
                op = base
            elif base[0] != "-":
                op = "-" + base
            else:
                op = base[1:]
        elif op in "+-x÷":
            if self.op2:
                base = self.calculate()
            self.operador = op
        elif op == "=":
            if not self.operador or self.op2 is None:
                op = base
            else:
                op = self.calculate()

        if not self.operador: 
            self.op1 = float(op)
        elif op in "+-x÷":
            op = base
        else:
            self.op2 = float(op)

        self.display.value = op
        print(f"{self.op1} {self.operador} {self.op2}")

    def calculate(self):
        if self.operador == "+":
            res = self.op1 + self.op2
        elif self.operador == "-":
            res = self.op1 - self.op2
        elif self.operador == "x":
            res = self.op1 * self.op2
        elif self.operador == "÷":
            res = self.op1 / self.op2

        if res == int(res):
            res = int(res)

        self.op1 = res
        self.op2 = None
        self.operador = None
        return f"{res}"


    def __createLayout(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(self.display)
        layout.addWidget(self.keypad)
        self.setLayout(layout)
        return layout

    def __init__(self):
        super().__init__()
        self.display = Display()
        self.keypad = KeyPad(len(self.buttons[0]), len(self.buttons))
        for lineNumber, line in enumerate(self.buttons):
            for colNumber, txt in enumerate(line):
                self.keypad.addWidget(txt, colNumber, lineNumber)
                self.keypad.connect(colNumber, lineNumber, self.operation)

        self.layout = self.__createLayout()
        self.op1 = 0
        self.op2 = None
        self.operador = None
