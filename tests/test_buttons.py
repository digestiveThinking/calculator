import pytest
from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication

from calculator.components import CalcButton

tv = None

def f(valor):
    global tv
    tv = valor

def anotherF(valor):
    global tv
    tv = valor + valor

@pytest.fixture
def widget(qtbot):
    the_widget = CalcButton("1", command = f)
    qtbot.addWidget(the_widget)

    return the_widget

def test_init_calcButton(widget):
    #Insertar boton en un contenedor para comprobar si es de tamaño fijo
    app = QApplication([])
    contenedor = QWidget()
    contenedor.setGeometry(0,0, 200, 40)
    layout = QVBoxLayout(contenedor)
    layout.addWidget(widget)
    contenedor.show()
    

    size = widget.geometry()
    assert size.height() == 60
    assert size.width() == 66


    

def test_clic_calcButton(widget, qtbot):
    value = qtbot.mouseClick(widget, Qt.MouseButton.LeftButton)
    assert tv == "1"

def test_change_command_calcbutton(widget, qtbot):
    widget.connect(anotherF)
    value = qtbot.mouseClick(widget, Qt.MouseButton.LeftButton)
    assert tv == "11"
