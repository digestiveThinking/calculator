from PyQt6.QtWidgets import QApplication

app = QApplication([])
app.setStyle('Fusion')

qss = "calculator/styles.qss"
with open(qss, "r") as fss:
    app.setStyleSheet(fss.read())
