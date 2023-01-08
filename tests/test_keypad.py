import pytest

from calculator.components import KeyPad
from PyQt6.QtCore import Qt

tv = None

def setValue(value):
    global tv
    tv = value

@pytest.fixture
def the_widget(qtbot):
    widget = KeyPad(4, 5)
    qtbot.addWidget(widget)

    return widget

def test_init_keypad(the_widget):
    assert the_widget.cols == 4
    assert the_widget.lines == 5
    for line in range(5):
        for col in range(4):
            assert the_widget.buttons[line][col] is None

def test_add_buttons_to_keypad(the_widget, qtbot):
    the_widget.addWidget("2", 3, 0)
    btn = the_widget.buttons[0][3]
    assert btn.text() == "2"
    the_widget.connect(3, 0, setValue)
    assert tv is None
    qtbot.mouseClick(btn, Qt.MouseButton.LeftButton)
    assert tv == "2"



