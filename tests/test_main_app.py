import pytest

from PyQt6.QtCore import Qt
from calculator.components import Calculator

@pytest.fixture
def app(qtbot):
    the_app = Calculator()
    qtbot.addWidget(the_app)

    return the_app

def test_has_display(app):
    assert app.display.text() == "0"

def test_display_show_clicked_numbers(app, qtbot):
    btn1 = app.keypad.buttons[3][0]
    assert btn1.text() == "1"
    assert app.display.text() == "0"
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "1"
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11"

def test_display_show_only_one_point(app, qtbot):
    btn1 = app.keypad.buttons[3][0]
    btnPoint = app.keypad.buttons[4][2]
    assert btn1.text() == "1"
    assert btnPoint.text() == "."
    assert app.display.text() == "0"
    qtbot.mouseClick(btnPoint, Qt.MouseButton.LeftButton)
    assert app.display.text() == "0."
    qtbot.mouseClick(btnPoint, Qt.MouseButton.LeftButton)
    assert app.display.text() == "0."
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "0.1"

def test_display_delete_last_char(app, qtbot):
    btn1 = app.keypad.buttons[3][0]
    btnPoint = app.keypad.buttons[4][2]
    btnDel = app.keypad.buttons[4][0]
    assert btn1.text() == "1"
    assert btnPoint.text() == "."
    assert btnDel.text() == "↩︎"
    assert app.display.text() == "0"
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(btnPoint, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11.11"
    qtbot.mouseClick(btnDel, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11.1"
    qtbot.mouseClick(btnDel, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11."
    qtbot.mouseClick(btnDel, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11"
    qtbot.mouseClick(btnDel, Qt.MouseButton.LeftButton)
    assert app.display.text() == "1"
    qtbot.mouseClick(btnDel, Qt.MouseButton.LeftButton)
    assert app.display.text() == "0"

def test_display_delete_all(app, qtbot):
    btn1 = app.keypad.buttons[3][0]
    btnC = app.keypad.buttons[0][0]
    assert btn1.text() == "1"
    assert btnC.text() == "C"
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11"
    qtbot.mouseClick(btnC, Qt.MouseButton.LeftButton)
    assert app.display.text() == "0"
    assert app.op1 == 0
    assert app.op2 is None
    assert app.operador is None

def test_display_change_of_sign(app, qtbot):
    btn1 = app.keypad.buttons[3][0]
    btnCS = app.keypad.buttons[0][1]
    assert btn1.text() == "1"
    assert btnCS.text() == "+/-"
    qtbot.mouseClick(btnCS, Qt.MouseButton.LeftButton)
    assert app.display.text() == "0"
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "1"
    qtbot.mouseClick(btnCS, Qt.MouseButton.LeftButton)
    assert app.display.text() == "-1"
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "-11"
    qtbot.mouseClick(btnCS, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11"


def test_adds(app, qtbot):
    btn1 = app.keypad.buttons[3][0]
    btnAdd = app.keypad.buttons[3][3]
    btnEq = app.keypad.buttons[4][3]
    assert btn1.text() == "1"
    assert btnAdd.text() == "+"
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11"
    qtbot.mouseClick(btnAdd, Qt.MouseButton.LeftButton)
    assert app.display.text() == "11"
    qtbot.mouseClick(btn1, Qt.MouseButton.LeftButton)
    assert app.display.text() == "1"
    qtbot.mouseClick(btnEq, Qt.MouseButton.LeftButton)
    assert app.display.text() == "12"






    

