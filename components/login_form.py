from databases.database_controller import connect_database
from models.person import Person
from components.admin_window import AdminWindow
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QLineEdit


con = connect_database()
user_data = Person()

class LoginForm(QtWidgets.QDialog):
    def __init__(self):
        super(LoginForm, self).__init__()
        uic.loadUi('components/form_base.ui', self)
        self.show()
        self.login_button = self.findChild(
            QtWidgets.QPushButton, 'login_button')
        self.login_button.clicked.connect(self.verifica_usuario)
        self.usuario: QLineEdit = self.findChild(QLineEdit, "username_input")
        self.senha: QLineEdit = self.findChild(QLineEdit, "password_input")
        self.email: QLineEdit = self.findChild(QLineEdit, "email_input")
        self.login_label: QtWidgets.QLabel = self.findChild(QtWidgets.QLabel, 'login_label')

    def verifica_usuario(self):
      usuario = self.usuario.text()
      senha = self.senha.text()
      email = self.email.text()

      if usuario and senha and email:
         copy_cur = con.cursor()
         copy_cur.execute("SELECT * FROM usuarios WHERE username=? AND email=? AND senha=md4(?);", [usuario, email, senha])
         resultado = copy_cur.fetchone()
         copy_cur.close()

         if resultado is not None:
            [id, name, lastname, password, username, email, tipo] = resultado
            print(id, name, name, lastname, password, username, email)
            self.login_label.setVisible(False)
            user_data.username = username
            print(user_data)
            if tipo == 'ADMIN':
               self.close()
               admin_screen = AdminWindow(user_data, self)
               admin_screen.show()


         else:
            print('Não encontrado')
            self.login_label.setVisible(True)
      else:
         print('Falta preencher os campos')
         self.login_label.setText('Você deve preencher todos os campos!')
         self.login_label.setVisible(True)