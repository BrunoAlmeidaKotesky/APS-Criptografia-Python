from components.menu import MainMenu
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   window = MainMenu()
   sys.exit(app.exec())

