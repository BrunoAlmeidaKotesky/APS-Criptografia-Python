
from databases.database_controller import connect_database
from PyQt5 import uic
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QTableWidget, QMainWindow, QPushButton, QLineEdit, QTableWidgetItem
from typing import TYPE_CHECKING
from models.person import Person


if TYPE_CHECKING:
    from components.login_form import LoginForm


class AdminWindow(QMainWindow):
   def __init__(self, person: Person, parent: 'LoginForm'):
        super(AdminWindow, self).__init__(parent)
        uic.loadUi('components/admin_menu.ui', self)
        self.username_label: QLabel = self.findChild(QLabel, 'lbl_username')
        user = person.username
        self.username_label.setText(
            'Bem vindo administrador {user}'.format(user=user))
        self.update_btn: QPushButton = self.findChild(
            QPushButton, 'btn_atualizar')
        self.delete_btn: QPushButton = self.findChild(QPushButton, 'btn_deletar')
        self.table: QTableWidget = self.findChild(QTableWidget, 'admin_table')
        self.delete_btn.clicked.connect(self.delete_row)
        self.load_table_data()

   def add_update_layout(self):
        user_input = QLineEdit()
        horizontalLayout: QHBoxLayout = self.findChild(
            QHBoxLayout, 'horizontalLayout_2')
        horizontalLayout.addWidget(user_input)

   def load_table_data(self):
       con = connect_database()
       cur = con.cursor()
       cur.execute(
           'SELECT id_user, nome_usuario, sobrenome_usuario, username, email, tipo FROM usuarios')
       all_rows = cur.fetchall()
       if len(all_rows) > 0:
          for idx, row in enumerate(all_rows):
              self.table.insertRow(idx)
              item = Person(row[0], row[1], row[2], row[5], row[3], row[4])
              self.set_table_data(item, idx)
          con.close()

   def set_table_data(self, item: Person, row_number: int):
        self.table.setItem(row_number, 0, QTableWidgetItem(str(item.id)))
        self.table.setItem(row_number, 1, QTableWidgetItem(item.username))
        self.table.setItem(row_number, 2, QTableWidgetItem(item.nome))
        self.table.setItem(row_number, 3, QTableWidgetItem(item.sobrenome))
        self.table.setItem(row_number, 4, QTableWidgetItem(item.email))
        self.table.setItem(row_number, 5, QTableWidgetItem(item.tipo))
   
   def delete_row(self):
       button = self.sender()
       if button:
          cur_row = self.table.currentRow()
          id = int((self.table.item(cur_row, 0).text()))
          con = connect_database()
          cur = con.cursor()
          cur.execute('DELETE FROM usuarios WHERE id_user=?', [id])
          con.commit()
          con.close()
          self.table.removeRow(cur_row)

        
    
