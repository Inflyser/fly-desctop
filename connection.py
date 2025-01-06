from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()
        
    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')
        
        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False
        
        query = QtSql.QSqlQuery()
        query.exec("""
                CREATE TABLE IF NOT EXISTS Bookings (
                    id CHAR(6) NOT NULL REFERENCES Airports(id),
                    book_ref CHAR(6),
                    book_date TIMESTAMP NOT NULL,
                    PRIMARY KEY (id, book_ref)
                );
                """)
        query.exec("""      
                CREATE TABLE IF NOT EXISTS Tickets (
                    id CHAR(6) NOT NULL REFERENCES Airports(id),
                    ticket_no CHAR(13),
                    book_ref CHAR(6) NOT NULL REFERENCES Bookings(book_ref),
                    passenger_id VARCHAR(20) NOT NULL,
                    passenger_name TEXT NOT NULL,
                    contact_data TEXT,
                    PRIMARY KEY (id, ticket_no)
                );
                """)
        query.exec("""  
                CREATE TABLE IF NOT EXISTS Airports (
                    id CHAR(6) PRIMARY KEY,
                    airport_code CHAR(3) NOT NULL,
                    airport_name TEXT NOT NULL,
                    city1 TEXT NOT NULL,
                    city2 TEXT NOT NULL,
                    longitude NUMERIC(9, 6) NOT NULL,
                    latitude NUMERIC(9, 6) NOT NULL
                );
                """)
        query.exec("""      
                CREATE TABLE IF NOT EXISTS Flights (
                    id CHAR(6) NOT NULL REFERENCES Airports(id),
                    flight_id SERIAL,
                    flight_no CHAR(3) NOT NULL,
                    scheduled_departure TIMESTAMP NOT NULL,
                    scheduled_arrival TIMESTAMP NOT NULL,
                    departure_airport CHAR(3) NOT NULL REFERENCES Airports(airport_code),
                    arrival_airport CHAR(3) NOT NULL REFERENCES Airports(airport_code),
                    status TEXT NOT NULL,
                    aircraft_code CHAR(3) NOT NULL REFERENCES Aircrafts(aircraft_code),
                    PRIMARY KEY (id, flight_id)
                );
                """)
        query.exec("""   
                CREATE TABLE IF NOT EXISTS Aircrafts (
                    id CHAR(6) NOT NULL REFERENCES Airports(id),
                    aircraft_code CHAR(3),
                    model TEXT NOT NULL,
                    PRIMARY KEY (id, aircraft_code)
                );
                """)
        query.exec("""     
                CREATE TABLE IF NOT EXISTS Seats (
                    id CHAR(6) NOT NULL REFERENCES Airports(id),
                    aircraft_code CHAR(3) NOT NULL REFERENCES Aircrafts(aircraft_code),
                    seat_no VARCHAR(3) NOT NULL,
                    fare_conditions TEXT NOT NULL,
                    PRIMARY KEY (aircraft_code, seat_no, id)
                );
                """)
        query.exec("""    
                CREATE TABLE IF NOT EXISTS Ticket_flights (
                    id CHAR(6) NOT NULL REFERENCES Airports(id),
                    ticket_no CHAR(13) NOT NULL REFERENCES Tickets(ticket_no),
                    flight_id INTEGER NOT NULL REFERENCES Flights(flight_id),
                    fare_conditions TEXT NOT NULL,
                    amount NUMERIC(10, 2) NOT NULL,
                    PRIMARY KEY (ticket_no, flight_id, id)
                );
                """)
        query.exec("""     
                CREATE TABLE IF NOT EXISTS Boarding_passes (
                    id CHAR(6) NOT NULL REFERENCES Airports(id),
                    ticket_no CHAR(13) NOT NULL REFERENCES Tickets(ticket_no),
                    flight_id INTEGER NOT NULL REFERENCES Flights(flight_id),
                    boarding_no INTEGER NOT NULL,
                    seat_no VARCHAR(4) NOT NULL,
                    PRIMARY KEY (ticket_no, flight_id, id)
                );                
            """)
        
        return True

    def execute_query_with_parans(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        
        query.exec()
        return query
    
    
       
    def add_new_tickets_query(self, id, ticket_no, book_ref, passenger_id, passenger_name, contact_data):
        sql_query = "INSERT INTO Tickets (id, ticket_no, book_ref, passenger_id, passenger_name, contact_data) VALUES (?, ?, ?, ?, ?, ?)"
        self.execute_query_with_parans(sql_query, [id, ticket_no, book_ref, passenger_id, passenger_name, contact_data])   
        
    def update_tickets_passenger_name(self, passenger_name, id1):
        sql_query = "UPDATE Tickets SET passenger_name=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [passenger_name, id1])  
        
    def update_tickets_book_ref(self, book_ref, id1):
        sql_query = "UPDATE Tickets SET book_ref=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [book_ref, id1]) 
        
    def delete_tickets_query(self, id1):
        sql_query = "DELETE FROM Tickets WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id1])  
        
    def update_flights_flight_id(self, flight_id, id1):
        sql_query = "UPDATE Flights SET flight_id=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [flight_id, id1]) 
    
    def update_flights_scheduled_departure(self, scheduled_departure, id1):
        sql_query = "UPDATE Flights SET scheduled_departure=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [scheduled_departure, id1]) 
        
    def update_flights_departure_airport(self, departure_airport, id1):
        sql_query = "UPDATE Flights SET departure_airport=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [departure_airport, id1]) 
        
    def update_flights_arrival_airport(self, arrival_airport, id1):
        sql_query = "UPDATE Flights SET arrival_airport=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [arrival_airport, id1]) 
    
    
    
    
    
    
    
    
    
    def add_new_flights_query(self, id, flight_id, flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, status, aircraft_code):
        sql_query = "INSERT INTO Flights (id, flight_id, flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, status, aircraft_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.execute_query_with_parans(sql_query, [id, flight_id, flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, status, aircraft_code])
    

    def delete_flights_query(self, id1):
        sql_query = "DELETE FROM Flights WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id1]) 
    
                
    def add_new_seats_query(self, id, aircraft_code, seat_no, fare_conditions):
        sql_query = "INSERT INTO Seats (id, aircraft_code, seat_no, fare_conditions) VALUES (?, ?, ?, ?)"
        self.execute_query_with_parans(sql_query, [id, aircraft_code, seat_no, fare_conditions])
        
    def update_seats_query(self, seat_no, id1):
        sql_query = "UPDATE Seats SET seat_no=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [seat_no, id1])  
    
    def delete_seats_query(self, id1):
        sql_query = "DELETE FROM Seats WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id1])  
    
    
    def add_new_boarding_passes_query(self, id, ticket_no, flight_id, boarding_no, seat_no):
        sql_query = "INSERT INTO Boarding_passes (id, ticket_no, flight_id, boarding_no, seat_no) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_parans(sql_query, [id, ticket_no, flight_id, boarding_no, seat_no])
    
    def update_boarding_passes_query(self, id, ticket_no, flight_id, boarding_no, seat_no, id1):
        sql_query = "UPDATE Boarding_passes SET id=?, ticket_no=?, flight_id=?, boarding_no=?, seat_no=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id, ticket_no, flight_id, boarding_no, seat_no, id1]) 
        
    def delete_boarding_passes_query(self, id1):
        sql_query = "DELETE FROM Boarding_passes WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id1])  
    
    
    def add_new_ticket_flights_query(self, id, ticket_no, flight_id, fare_conditions, amount):
        sql_query = "INSERT INTO Ticket_flights (id, ticket_no, flight_id, fare_conditions, amount) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_parans(sql_query, [id, ticket_no, flight_id, fare_conditions, amount])
        
    def update_ticket_flights_query(self, id, ticket_no, flight_id, fare_conditions, amount, id1):
        sql_query = "UPDATE Ticket_flights SET id=?, ticket_no=?, flight_id=?, fare_conditions=?, amount=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id, ticket_no, flight_id, fare_conditions, amount, id1]) 
   
    def delete_ticket_flights_query(self, id1):
        sql_query = "DELETE FROM Ticket_flights WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id1])    
        
             
    def add_new_aircraft_query(self, id, aircraft_code, model):
        sql_query = "INSERT INTO Aircrafts (id, aircraft_code, model) VALUES (?, ?, ?)"
        self.execute_query_with_parans(sql_query, [id, aircraft_code, model])

    def update_aircraft_query(self, id, aircraft_code, model, id1):
        sql_query = "UPDATE Aircrafts SET id=?, aircraft_code=?, model=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id, aircraft_code, model, id1]) 
        
    def delete_aircraft_query(self, id1):
        sql_query = "DELETE FROM Aircrafts WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id1])  
        
        
        
    def update_airports_city1_query(self, city1, id1):
        sql_query = "UPDATE Airports SET city1=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [city1, id1])   
    
    def update_airports_city2_query(self, city2, id1):
        sql_query = "UPDATE Airports SET city2=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [city2, id1])   

    def add_new_airports_query(self, id, airport_code, airport_name, city1, city2, longitude, latitude):
        sql_query = "INSERT INTO Airports (id, airport_code, airport_name, city1, city2, longitude, latitude) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.execute_query_with_parans(sql_query, [id, airport_code, airport_name, city1, city2, longitude, latitude])
    
    def update_airports_query(self, id, airport_code, airport_name, city1, city2, longitude, latitude, id1):
        sql_query = "UPDATE Airports SET id=?, airport_code=?, airport_name=?, city1=?, city2=?, longitude=?, latitude=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id, airport_code, airport_name, city1, city2, longitude, latitude, id1])  
        
    def delete_airports_query(self, id1):
        sql_query = "DELETE FROM Airports WHERE ID=?"
        self.execute_query_with_parans(sql_query, [id1])
    
    
    def add_new_transaction_query(self, id, book_ref, book_date):
        sql_query = "INSERT INTO Bookings (id, book_ref, book_date) VALUES (?, ?, ?)"
        self.execute_query_with_parans(sql_query, [id, book_ref, book_date])
        
    def update_bookings_query(self, book_ref, id1):
        sql_query = "UPDATE Bookings SET book_ref=? WHERE ID=?"
        self.execute_query_with_parans(sql_query, [book_ref, id1])   
        
    def delete_transaction_query(self, id1):
        sql_query = "DELETE FROM Bookings WHERE ID=?"
        try:
            self.execute_query_with_parans(sql_query, [id1])
            print(f"Запись с ID {id1} успешно удалена.")
        except Exception as e:
            print(f"Ошибка при удалении записи с ID {id1}: {e}")
 
   