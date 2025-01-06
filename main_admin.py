import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_table_new import Ui_MainWindow
from ui_edit_last import Ui_Dialog as Ui_EditDialog

from connection import Data

from datetime import datetime


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        
        self.view_data()
        

        # self.ui_edit.lineEdit.setPlaceholderText("Новый текст-заполнитель")
        
        self.ui.lineEdit_4.textChanged.connect(self.date_sort)
        self.ui.lineEdit_5.textChanged.connect(self.date_sort)
      
        
       
        self.ui.nextButton_3.clicked.connect(self.open_new_edit_window)
        self.ui.nextButton_3.clicked.connect(self.select_ticket)
        self.ui.nextButton_2.clicked.connect(self.delete_query)
        
        
    
    def open_new_edit_window(self):
        self.edit_window = QtWidgets.QDialog()
        self.ui_edit = Ui_EditDialog()
        self.ui_edit.setupUi(self.edit_window)
        self.edit_window.show()
        
        if self.ui.lineEdit.text() != "" and self.ui.lineEdit.text() != " ":
            global id_index
            id_index = int(self.ui.lineEdit.text())
            ID = id_index
            if len(str(ID)) == 3: n = "ID:" + str(ID)
            elif len(str(ID)) == 2: n = "ID:" + "0" + str(ID) 
            else: n = "ID:" + "00" + str(ID)
            ID = n  
            self.ui_edit.label_2.setText(f"{ID}")
        
        
            
        self.ui_edit.nextButton_5.clicked.connect(self.exit_edit)
        self.ui_edit.nextButton_4.clicked.connect(self.save_edit)
        
        self.view_data()
       
        
    def view_data(self):
        global table1, table, row_count,table2
        self.model = QSqlTableModel(self)
        table_name = ["Bookings", "Tickets", "Airports", "Flights", "Aircrafts",
                      "Seats", "Ticket_flights", "Boarding_passes"]     
   
        
        add_all_data = []
        def plant():
            add_data = []  
            for row in range(self.model.rowCount()):  
                row_data = [] 
                for column in range(self.model.columnCount()): 
                    item = self.model.record(row).value(column)  
                    row_data.append(item)
                add_data.append(row_data)  
            return add_data
        
        
        for i in table_name:
            self.model.setTable(i)
            self.model.select()
            add_all_data.append(plant())
            row_count = self.model.rowCount()
      
        table = []
        
        for i in range(len(add_all_data)):
            table.append([table_name[i], add_all_data[i]])
        
  
     
        try:
            table1 = []
            for index in range(1, row_count+1):
                table1.append([table[0][1][index-1][0], table[1][1][index-1][4], table[3][1][index-1][3], table[3][1][index-1][1], \
                    table[3][1][index-1][5], table[2][1][index-1][3], table[2][1][index-1][1] + "\n" + table[2][1][index-1][4], table[3][1][index-1][6],\
                        table[0][1][index-1][1], table[5][1][index-1][2]])
        
          
            self.model.clear()
            self.model = QStandardItemModel(len(table1), len(table1[0]), self)

            for row in range(len(table1)):
                for column in range(len(table1[row])):
                    item = QStandardItem(str(table1[row][column]))
                    self.model.setItem(row, column, item)

            # Установка модели в QTableView
            self.ui.tableView.setModel(self.model)
        except IndexError:
            pass
        
        table2 = table1


    def select_ticket(self):  
        l = []
        name1 = table1[id_index-1][1]
        if name1.count(" ") > 1:
            for i in range(len(name1)):
                if name1[i] == " ": l.append(i)
            passenger_name0 = ((f"{name1[:l[0]]}\n{name1[l[0]+1:l[1]]}"))
        elif name1.count(" ") == 1:
            for i in range(len(name1)):
                if name1[i] == " ": l.append(i)
            passenger_name0 = ((f"{name1[:l[0]]}\n{name1[l[0]+1:]}"))
        else: passenger_name0 = (f"{name1}")
            
        self.ui_edit.name.setText(f"{passenger_name0}")
        self.ui_edit.number.setText(f"{table1[id_index-1][3]}")
        self.ui_edit.date1.setText(f"{table1[id_index-1][2]}")
        self.ui_edit.time1.setText(f"{table1[id_index-1][4]}")
        self.ui_edit.city1.setText(f"{table1[id_index-1][5]}")
        self.ui_edit.city2.setText(f"{table1[id_index-1][6]}")
        self.ui_edit.time2.setText(f"{table1[id_index-1][7]}")
        self.ui_edit.code_pnr.setText(f"{table1[id_index-1][8]}")
        self.ui_edit.seat.setText(f"{table1[id_index-1][9]}") 
        self.view_data()
    
    def date_sort(self):
        global table1
        self.ui.lineEdit_4.setPlaceholderText("Name")
        self.ui.lineEdit_5.setPlaceholderText("Date")
        prefix = self.ui.lineEdit_4.text()
        prefix1 = self.ui.lineEdit_5.text()
        
        # Фильтруем записи по имени
        if len(prefix) != 0:
            table13 = [
                record for record in table1 if record[1].startswith(prefix)
            ]
        if len(prefix1) != 0:
            table12 = [
                record for record in table1 if record[2][:-1].startswith(prefix1)
            ]
      
        if (len(prefix1) != 0) and (len(prefix) != 0):     
            table1 = [list(item) for item in set(tuple(sublist) for sublist in table13) & set(tuple(sublist) for sublist in table12)]
         
        else:
            if len(prefix) != 0:
                table1 = table13
            if len(prefix1) != 0:
                table1 = table12
  
        
        if len(table1) == 0:
            if (len(prefix1) != 0) and (len(prefix) != 0) or (len(prefix1) != 0) and (len(prefix) == 0):
                table1 = table2
                self.ui.lineEdit_5.clear()
                self.ui.lineEdit_5.setPlaceholderText("Error")
            if (len(prefix1) != 0) and (len(prefix) != 0) or (len(prefix) != 0) and (len(prefix1) == 0):
                table1 = table2
                self.ui.lineEdit_4.clear()
                self.ui.lineEdit_4.setPlaceholderText("Error")

            if (len(prefix1) != 0) and (len(prefix) != 0):  
                table1 = table2
      
        self.model = QSqlTableModel(self)

        self.model.clear()
        self.model = QStandardItemModel(len(table1), len(table1[0]), self)
        for row in range(len(table1)):
            for column in range(len(table1[row])):
                item = QStandardItem(str(table1[row][column]))
                self.model.setItem(row, column, item)
        
        self.ui.tableView.setModel(self.model)
  
        table1 = table2
        table13 = []
        table12 = []
        
        
    def exit_edit(self):
        self.view_data()
        self.edit_window.close()
        
    def save_edit(self):
  
        if self.ui.lineEdit.text() != "" and self.ui.lineEdit.text() != " ":
            id_index = int(self.ui.lineEdit.text())
            index1 = id_index-1
        index = self.model.index(id_index-1, 0)  # row и column - это номера строки и столбца
        self.ui.tableView.setCurrentIndex(index)
        id = str(self.ui.tableView.model().data(self.ui.tableView.model().index(index.row(), 0)))
        
        if self.ui_edit.lineEdit.text():
            self.conn.update_tickets_passenger_name(self.ui_edit.lineEdit.text(), id)
        if self.ui_edit.lineEdit_8.text():
            self.conn.update_tickets_book_ref(self.ui_edit.lineEdit_8.text(), id)    
        if self.ui_edit.lineEdit_3.text():
            self.conn.update_flights_flight_id(self.ui_edit.lineEdit_3.text(), id)  
        if self.ui_edit.lineEdit_2.text():
            self.conn.update_flights_scheduled_departure(self.ui_edit.lineEdit_2.text(), id)
        if self.ui_edit.lineEdit_4.text():
            self.conn.update_flights_departure_airport(self.ui_edit.lineEdit_4.text(), id)  
        if self.ui_edit.lineEdit_7.text():
            self.conn.update_flights_arrival_airport(self.ui_edit.lineEdit_7.text(), id) 
        if self.ui_edit.lineEdit_8.text():
            self.conn.update_bookings_query(self.ui_edit.lineEdit_8.text(), id) 
        if self.ui_edit.lineEdit_9.text():
            self.conn.update_seats_query(self.ui_edit.lineEdit_9.text(), id) 
        if self.ui_edit.lineEdit_6.text():
            self.conn.update_airports_city2_query(self.ui_edit.lineEdit_6.text(), id) 
        if self.ui_edit.lineEdit_10.text():
            self.conn.update_airports_city1_query(self.ui_edit.lineEdit_10.text(), id) 
        

  
        
        self.select_ticket()
        self.view_data()
        
        self.ui_edit.lineEdit.clear()
        self.ui_edit.lineEdit_2.clear()
        self.ui_edit.lineEdit_3.clear()
        self.ui_edit.lineEdit_4.clear()
        self.ui_edit.lineEdit_6.clear()
        self.ui_edit.lineEdit_7.clear()
        self.ui_edit.lineEdit_8.clear()
        self.ui_edit.lineEdit_9.clear()
        
        
        
# passenger_name scheduled_departure flight_id departure_airport city1 city2 arrival_airport book_ref seat_no

    def delete_query(self):
        if self.ui.lineEdit.text() != "" and self.ui.lineEdit.text() != " ":
            id_index = int(self.ui.lineEdit.text())
     

        index = self.model.index(id_index-1, 0)  # row и column - это номера строки и столбца
        self.ui.tableView.setCurrentIndex(index)
        id = str(self.ui.tableView.model().data(self.ui.tableView.model().index(index.row(), 0)))
        self.conn.delete_transaction_query(id)
        self.conn.delete_airports_query(id)
        self.conn.delete_aircraft_query(id)
        self.conn.delete_ticket_flights_query(id)
        self.conn.delete_boarding_passes_query(id)
        self.conn.delete_seats_query(id)
        self.conn.delete_flights_query(id)
        self.conn.delete_tickets_query(id)
        
      
        self.view_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    
    sys.exit(app.exec())