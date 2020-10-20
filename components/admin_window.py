import components.menu as menu
from databases.database_controller import connect_database
from PyQt5 import uic
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QTableWidget, QMainWindow, QPushButton, QLineEdit, QTableWidgetItem, QItemDelegate
from typing import TYPE_CHECKING
from models.person import Person

if TYPE_CHECKING:
    from components.login_form import LoginForm

class AdminWindow(QMainWindow):
   def __init__(self, person: Person, parent: 'LoginForm'):
        super(AdminWindow, self).__init__(parent)
        uic.loadUi('components/admin_menu.ui', self)
        self.username_label: QLabel = self.findChild(QLabel, 'lbl_username')
        self.user_data = person
        self.username_label.setText(f'Bem vindo administrador {person.username}')
        self.update_btn: QPushButton = self.findChild(QPushButton, 'btn_atualizar')
        self.delete_btn: QPushButton = self.findChild(QPushButton, 'btn_deletar')
        self.add_btn: QPushButton = self.findChild(QPushButton, 'btn_cadastrar')
        self.table: QTableWidget = self.findChild(QTableWidget, 'admin_table')
        self.delete_btn.clicked.connect(self.delete_row)
        self.update_btn.clicked.connect(self.update_row)
        self.add_btn.clicked.connect(self.open_sign_up)
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
          
   def open_sign_up(self):
       if self.user_data:
           self.form = menu.RegisterForm(self.user_data)
           self.close()
           self.form.show()
   
   def get_current_row(self) -> Person:
       button = self.sender()
       if button:
           cur_row = self.table.currentRow()
           id = int((self.table.item(cur_row, 0).text()))
           username = self.table.item(cur_row, 1).text()
           nome = self.table.item(cur_row, 2).text()
           sobrenome = self.table.item(cur_row, 3).text()
           email = self.table.item(cur_row, 4).text()
           tipo = self.table.item(cur_row, 5).text()
           return Person(id, nome, sobrenome, tipo, username, email)

   def update_row(self):
       person_data = self.get_current_row()
       if person_data:
          con = connect_database()
          cur = con.cursor()
          cur.execute('''
            UPDATE usuarios 
            SET nome_usuario=?, sobrenome_usuario=?, username=?, email=?, tipo=?  
            WHERE id_user=?''', [
                person_data.nome,
                person_data.sobrenome,
                person_data.username,
                person_data.email, 
                person_data.tipo, 
                person_data.id
            ])
          con.commit()
          self.username_label.setText('Atualizado com sucesso!')
          con.close()
