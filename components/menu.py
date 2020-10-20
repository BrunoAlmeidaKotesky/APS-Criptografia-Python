from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel
from components.login_form import LoginForm
from databases.database_controller import connect_database
from models.person import Person

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



con = connect_database()
user_data = Person()

class RegisterForm(QMainWindow):
    def __init__(self, person: Person = None):
        super(RegisterForm, self).__init__()
        uic.loadUi('components/sign_up.ui', self)
        self.show()
        self.user_type:str = None
        if person is not None:
            self.user_type = person.tipo
        self.user_name:QLineEdit = self.findChild(QLineEdit, 'lineEdit')
        self.nome:QLineEdit = self.findChild(QLineEdit, 'lineEdit_2')
        self.sobrenome:QLineEdit = self.findChild(QLineEdit, 'lineEdit_3')
        self.email:QLineEdit = self.findChild(QLineEdit, 'lineEdit_4')
        self.senha:QLineEdit = self.findChild(QLineEdit, 'lineEdit_5')
        self.button:QPushButton = self.findChild(QPushButton, 'cadastrar_btn')
        self.label:QLabel = self.findChild(QLabel, 'status_message')
        self.button.clicked.connect(self.register_new_user)

    def register_new_user(self):
        values_list = [self.user_name.text(), self.nome.text(), self.sobrenome.text(), self.email.text(), self.senha.text()]
        cur = con.cursor()
        if all((value is not None and len(value) > 0) for value in values_list):
            username = values_list[0]
            nome_usuario = values_list[1]
            sobrenome_usuario = values_list[2]
            senha = values_list[4]
            email = values_list[3]
            cur.execute('SELECT email from usuarios WHERE email=?', [values_list[4]])
            result = cur.fetchone()
            cur.close()
            if result:
                self.label.setText('Já existe um usuário com este e-mail cadastrado!')
            else:
                insert_cur = con.cursor()
                tipo = self.user_type if self.user_type is not None else 'USUARIO'
                insert_cur.execute("INSERT INTO usuarios VALUES (?, ?, ?, md4(?), ?, ?, ?)", [None, nome_usuario, sobrenome_usuario, senha, username, email, tipo])
                con.commit()
                self.label.setText('Usuário criado com sucesso!')
                self.user_name.setText('')
                self.nome.setText('')
                self.sobrenome.setText('')
                self.email.setText('')
                self.senha.setText('')
                self.menu = MainMenu()
                self.menu.show()
                self.hide()
