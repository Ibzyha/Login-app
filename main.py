import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import bg
import icons
class login(QDialog):
    def __init__(self):
        super(login, self).__init__()
        loadUi("Login.ui", self)
app = QApplication(sys.argv)
app.setApplicationName("Login app | made by ibzzy")
log = login()
widget = QStackedWidget()
widget.addWidget(log)
widget.setFixedHeight(400)
widget.setFixedWidth(708)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting..")