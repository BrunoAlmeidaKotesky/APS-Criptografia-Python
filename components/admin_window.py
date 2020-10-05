
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QLabel, QHBoxLayout
from typing import TYPE_CHECKING
from models.person import Person

if TYPE_CHECKING:
    from components.login_form import LoginForm

class AdminWindow(QtWidgets.QMainWindow):
   def __init__(self, person: Person, parent: 'LoginForm'):
        super(AdminWindow, self).__init__(parent)
        uic.loadUi('components/admin_menu.ui', self)
        self.username_label: QLabel = self.findChild(QLabel, 'lbl_username')
        user = person.ususername
        self.username_label.setText('Bem vindo administrador {user}'.format(user=user))
        self.update_btn = self.findChild(QtWidgets.QPushButton, 'btn_atualizar')
        #   self.update_btn.clicked.connect(self.add_update_layout())

   def add_update_layout(self):
      user_input = QtWidgets.QLineEdit()
      horizontalLayout:QHBoxLayout = self.findChild(QHBoxLayout, 'horizontalLayout_2')
      horizontalLayout.addWidget(user_input)