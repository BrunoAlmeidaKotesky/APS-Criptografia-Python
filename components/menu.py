from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton
from components.login_form import LoginForm
from components.sign_up import RegisterForm

class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        uic.loadUi('components/menu.ui', self)
        self.show()
        self.btn_login:QPushButton = self.findChild(QPushButton, 'login_btn')
        self.cadastrar_btn:QPushButton = self.findChild(QPushButton, 'register_btn')
        self.btn_login.clicked.connect(self.open_login)
        self.cadastrar_btn.clicked.connect(self.open_sign_up)

    def open_login(self):
        self.login = LoginForm()
        self.login.show()
        self.hide()
    
    def open_sign_up(self):
        self.register = RegisterForm()
        self.register.show()
        self.hide()