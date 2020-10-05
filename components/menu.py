from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton
from components.login_form import LoginForm

class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        uic.loadUi('components/menu.ui', self)
        self.show()
        self.btn_login:QPushButton = self.findChild(QPushButton, 'login_btn')
        self.cadastrar_btn:QPushButton = self.findChild(QPushButton, 'register_btn')
        self.btn_login.clicked.connect(self.open_login)

    def open_login(self):
        self.login = LoginForm()
        self.login.show()
        self.hide()