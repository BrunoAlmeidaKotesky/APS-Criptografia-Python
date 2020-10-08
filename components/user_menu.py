from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog

class UserMenu(QDialog):
     def __init__(self):
        super(UserMenu, self).__init__()
        uic.loadUi('components/user_menu.ui', self)
        self.show()