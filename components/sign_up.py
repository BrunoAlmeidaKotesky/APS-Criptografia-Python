from databases.database_controller import connect_database
from models.person import Person
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel


con = connect_database()
user_data = Person()

class RegisterForm(QMainWindow):
    def __init__(self):
        super(RegisterForm, self).__init__()
        uic.loadUi('components/sign_up.ui', self)
        self.user_name:QLineEdit = self.findChild(QLineEdit, 'lineEdit')
        self.nome:QLineEdit = self.findChild(QLineEdit, 'lineEdit_2')
        self.sobrenome:QLineEdit = self.findChild(QLineEdit, 'lineEdit_3')
        self.email:QLineEdit = self.findChild(QLineEdit, 'lineEdit_4')
        self.senha:QLineEdit = self.findChild(QLineEdit, 'lineEdit_5')
        self.button:QPushButton = self.findChild(QPushButton, 'cadastrar_btn')
        self.label:QLabel = self.findChild(QLabel, 'status_message')


    def register_new_user(self):
        values_list = [self.user_name.text(), self.nome.text(), self.sobrenome.text(), self.email.text(), self.senha.text()]
        if all((value is not None and len(value) > 0) for value in values_list):
            print('')
