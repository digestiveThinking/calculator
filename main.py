import sys
from calculator import app
from calculator.components import Calculator

calculator = Calculator()
calculator.show()   
sys.exit(app.exec())