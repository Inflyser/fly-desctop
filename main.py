import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_MainWindow
from ui_tarif import Ui_Dialog as Ui_TarifDialog
from ui_date import Ui_Dialog as Ui_DateDialog
from ui_sum import Ui_Dialog as Ui_SumDialog
from ui_contact import Ui_Dialog as Ui_ContactDialog
from ui_ticket1 import Ui_Dialog as Ui_TicketDialog

from connection import Data

from script_date import Data_time
from data import ID0, Book_ref, Book_date, City_distance, Airport_code_airport_name,\
    Aircraft_code_model, Ticket_no, Flight_no, Flight_id, Amount, Boarding_no, Seat_no,\
    Passenger_id

ID = next(ID0())
range1 = 0

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        
       
        self.ui.Button_next.clicked.connect(self.add_object_all)
        self.ui.Button_next.clicked.connect(self.open_new_tarif_window)
        
        
        self.ui.where1.currentTextChanged.connect(self.allp)
            
        
    def view_data(self):
        global ID
        self.model = QSqlTableModel(self)
        self.model.setTable("Bookings")
        self.model.select()  # Загружаем данные из таблицы

        if self.model.rowCount() > 0:  
            last_row_index = self.model.rowCount() - 1  
            record = self.model.record(last_row_index)   
            booking_id = record.value("id")             
            ID = int(booking_id[3:])+1
            if len(str(ID)) == 3: n = "ID:" + str(ID)
            elif len(str(ID)) == 2: n = "ID:" + "0" + str(ID) 
            else: n = "ID:" + "00" + str(ID)
            ID = n
                    
      
    def open_new_tarif_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_TarifDialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
  
        self.ui_window.nextButton.clicked.connect(self.add_object_tarif)
        self.ui_window.nextButton.clicked.connect(self.open_new_date_window) 
        
            
    def open_new_date_window(self):
        self.new_window_date = QtWidgets.QDialog()
        self.ui_date = Ui_DateDialog()
        self.ui_date.setupUi(self.new_window_date)
        self.new_window_date.show()
       
        self.ui_date.nextButton.clicked.connect(self.add_object_date)
        self.ui_date.nextButton.clicked.connect(self.open_new_sum_window)
        self.ui_date.nextButton.clicked.connect(self.select_sum)
    
    def open_new_sum_window(self):
        self.new_window_sum = QtWidgets.QDialog()
        self.ui_sum = Ui_SumDialog()
        self.ui_sum.setupUi(self.new_window_sum)
        self.new_window_sum.show()
       
        self.ui_sum.nextButton.clicked.connect(self.add_object_sum)
        self.ui_sum.nextButton.clicked.connect(self.open_new_contact_window)
        
    def open_new_contact_window(self):
        self.new_window_contact = QtWidgets.QDialog()
        self.ui_contact = Ui_ContactDialog()
        self.ui_contact.setupUi(self.new_window_contact)
        self.new_window_contact.show()
       
        self.ui_contact.nextButton.clicked.connect(self.add_object_contact)
        self.ui_contact.nextButton.clicked.connect(self.open_new_ticket_window)
        self.ui_contact.nextButton.clicked.connect(self.select_ticket)
 
    def open_new_ticket_window(self):
        self.new_window_ticket = QtWidgets.QDialog()
        self.ui_ticket = Ui_TicketDialog()
        self.ui_ticket.setupUi(self.new_window_ticket)
        self.new_window_ticket.show()
       
        self.ui_ticket.nextButton_2.clicked.connect(self.add_object_ticket)
        
        
    def allp(self):
        global city1, city2, city_distance, range1
        city1 = self.ui.where1.currentText() # откуда
        city2 = self.ui.where2.currentText() # куда
        
        city_distance = City_distance(city1, city2)
        range1 = city_distance[0]
        self.ui.round.setText(f"{range1}")
        
    def add_object_all(self): # МЕИН _ ДАТА
        self.view_data()
        window.hide()
       
        
    def add_object_tarif(self): # ТАРИФ _ ДАТА
        global range1, aircraft_code, ID, flight_id, amount, book_ref, ticket_no, seat_no
        aircraft_code = Aircraft_code_model()[0]
        model = Aircraft_code_model()[1]
        Airport = Airport_code_airport_name(city2)  
        airport_code = Airport[0]
        # Airport_code_airport_name(city2)
        self.conn.add_new_airports_query(ID, airport_code, Airport[1],\
            city1, city2, city_distance[1], city_distance[2])
        self.conn.add_new_aircraft_query(ID, aircraft_code, model)
       
        fare_conditions = self.ui_window.comboBox.currentText()
        ticket_no = Ticket_no()
        flight_id = Flight_id()
        seat_no = Seat_no()
        book_ref = Book_ref()
        amount = Amount(range1, fare_conditions)
        
        self.conn.add_new_transaction_query(ID, book_ref, Book_date())
        self.conn.add_new_ticket_flights_query(ID, ticket_no, flight_id, fare_conditions, amount)
        self.conn.add_new_boarding_passes_query(ID, ticket_no, flight_id, Boarding_no(), seat_no)
        self.conn.add_new_seats_query(ID, aircraft_code, seat_no, fare_conditions)
        
        self.new_window.close()
      
        
    def add_object_date(self): # ТАРИФ _ ДАТА
        global departure_airport, arrival_airport, scheduled_departure, scheduled_arrival
        date_plane = self.ui_date.calendarWidget.selectedDate()
        formatted_date = date_plane.toString("dd.MM.yyyy")
        date = Data_time(int(range1 / 10), formatted_date)
        print(date[0], date[1]) # время отправки и время прибытия
        # Дата
        index1 = date[0].find(":")
        scheduled_departure = date[0][:index1-2]
        scheduled_arrival = date[1][:index1-2]
        # Время
        index2 = date[1].find(":")
        departure_airport = date[0][index2-2:]
        arrival_airport = date[1][index2-2:]
        
        self.conn.add_new_flights_query(ID, flight_id, Flight_no(), scheduled_departure, \
            scheduled_arrival, departure_airport, arrival_airport,\
                "ожидание отправления", aircraft_code)
        
        self.new_window_date.close()
    
    
    def select_sum(self):
        self.ui_sum.sum.setText(f"{amount}")
        self.ui_sum.time1.setText(f"{departure_airport}")
        self.ui_sum.time2.setText(f"{arrival_airport}")
        self.ui_sum.date1.setText(f"{scheduled_departure}")
        self.ui_sum.date2.setText(f"{scheduled_arrival}")
        self.ui_sum.city1.setText(f"{city1}")
        self.ui_sum.city2.setText(f"{city2}")
        self.ui_sum.booking_12.setText(f"{city1}-{city2}")
        self.ui_sum.booking_13.setText(f"{round((range1 / 600), 2) } h")
        
    
    def add_object_sum(self):   
        self.new_window_sum.close()
        
    def add_object_contact(self):
        global passenger_name, passenger_id
        passenger_name = self.ui_contact.name.text()
        contact_data = self.ui_contact.email.text()
        passenger_id = Passenger_id()
     
        self.conn.add_new_tickets_query(ID, ticket_no, book_ref, passenger_id, passenger_name, contact_data)
        
    
        self.new_window_contact.close()
    
    def select_ticket(self):  
        l = []
        if passenger_name.count(" ") > 1:
            for i in range(len(passenger_name)):
                if passenger_name[i] == " ": l.append(i)
            passenger_name0 = ((f"{passenger_name[:l[0]]}\n{passenger_name[l[0]+1:l[1]]}"))

        elif passenger_name.count(" ") == 1:
            for i in range(len(passenger_name)):
                if passenger_name[i] == " ": l.append(i)
            passenger_name0 = ((f"{passenger_name[:l[0]]}\n{passenger_name[l[0]+1:]}"))
        else: passenger_name0 = (f"{passenger_name}")
            
        self.ui_ticket.name.setText(f"{passenger_name0}")
        self.ui_ticket.number.setText(f"{flight_id}")
        self.ui_ticket.date1.setText(f"{scheduled_departure}")
        self.ui_ticket.time1.setText(f"{departure_airport}")
        self.ui_ticket.city1.setText(f"{Airport_code_airport_name(city1)[0]}\n{city1}")
        self.ui_ticket.city2.setText(f"{Airport_code_airport_name(city2)[0]}\n{city2}")
        self.ui_ticket.time2.setText(f"{arrival_airport}")
        self.ui_ticket.code_pnr.setText(f"{book_ref}")
        self.ui_ticket.title_25.setText(f"{passenger_id[0]}{passenger_id[1]}")
        self.ui_ticket.seat.setText(f"{seat_no}")
    
    def add_object_ticket(self):
        
        self.new_window_ticket.close()
        window.show()
 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    
    sys.exit(app.exec())