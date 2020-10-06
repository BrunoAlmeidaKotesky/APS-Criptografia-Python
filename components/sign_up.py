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
        self.show()
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
            if result:
                self.label.setText('Já existe um usuário com este e-mail cadastrado!')
            else:
                cur.execute("INSERT INTO usuarios VALUES (?, ?, ?, md4(?), ?, ?, ?)", [None, nome_usuario, sobrenome_usuario, senha, username, email, 'USUARIO'])
                con.commit()
                self.label.setText('Usuário criado com sucesso!')
                self.user_name.setText('')
                self.nome.setText('')
                self.sobrenome.setText('')
                self.email.setText('')
                self.senha.setText('')
                self.clear_label()
    
    def clear_label(self):
        self.label.setText('')