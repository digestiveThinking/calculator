import pytest

from calculator.components import Display

@pytest.fixture
def the_widget(qtbot):
    widget = Display()
    qtbot.addWidget(widget)

    return widget

def test_init_display(the_widget):
    assert the_widget.value == 0.0
    the_widget.value = 12
    assert the_widget.value == 12.0
    the_widget.value = -3.123
    assert the_widget.value == -3.123

def test_value_error_display(the_widget):
    with pytest.raises(ValueError):
        the_widget.value = "Hola"
