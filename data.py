import random, string, time
from script_km import Distance

def ID0(ID = []):
    for i in range(1, 1000):
        if len(str(i)) == 3:
            n = "ID:" + str(i)
        elif len(str(i)) == 2:
            n = "ID:" + "0" + str(i) 
        else: 
            n = "ID:" + "00" + str(i)
        ID.append(n)
    return iter(ID)

def Book_ref():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

def Book_date():
    return time.ctime()

def City_distance(city1, city2):
    # ДЛИНА ПЕРЕЛЕТА
    range_place = Distance(city1, city2) # фунция подсчета расстояния
    range1 = range_place[0] # длина перелета км

    longitude = range_place[1][1] # долгота
    latitude = range_place[1][0] # широта
    return range1, longitude, latitude

def Airport_code_airport_name(city):
    Airport = [
            ["Амстердам", "AMS", "Amsterdam Airport Schiphol"],
            ["Барселона", "BCN", "Barcelona-El Prat Airport"],
            ["Бангкок", "BKK", "Suvarnabhumi Airport"],
            ["Берлин", "BER", "Berlin Brandenburg Airport"],
            ["Будапешт", "BUD", "Budapest Ferenc Liszt International Airport"],
            ["Дубай", "DXB", "Dubai International Airport"],
            ["Кейптаун", "CPT", "Cape Town International Airport"],
            ["Калининград", "KGD", "Khrabrovo Airport"],
            ["Лиссабон", "LIS", "Lisbon Portela Airport"],
            ["Лондон", "LON", "мегакод, включает несколько аэропортов: Heathrow, Gatwick и др."],
            ["Лос-Анджелес", "LAX", "Los Angeles International Airport"],
            ["Мадрид", "MAD", "Adolfo Suárez Madrid-Barajas Airport"],
            ["Милан", "MXP", "Milan Malpensa Airport"],
            ["Москва", "SVO / DME / VKO", "Sheremetyevo / Domodedovo / Vnukovo International Airports"],
            ["Мюнхен", "MUC", "Munich Airport"],
            ["Нью-Йорк", "NYC", "мегакод, включает несколько аэропортов: JFK, LaGuardia и др."],
            ["Осака", "KIX", "Kansai International Airport"],
            ["Париж", "CDG", "Charles de Gaulle Airport"],
            ["Пальма-де-Майорка", "PMI", "Palma de Mallorca Airport"],
            ["Прага", "PRG", "Václav Havel Airport Prague"],
            ["Рим", "FCO", "Leonardo da Vinci International Airport"],
            ["Севилья", "SVQ", "Seville San Pablo Airport"],
            ["Сидней", "SYD", "Sydney Kingsford Smith Airport"],
            ["Сингапур", "SIN", "Singapore Changi Airport"],
            ["Сеул", "ICN", "Incheon International Airport"],
            ["Токио", "NRT / HND", "Narita / Haneda Airports"],
            ["Тайбэй", "TPE", "Taiwan Taoyuan International Airport"],
            ["Чикаго", "ORD", "O'Hare International Airport"],
            ["Вена", "VIE", "Vienna International Airport"],
            ["Марракеш", "RAK", "Marrakech Menara Airport"]
        ]
    for i in Airport:
        if i[0] == city:
            return i[1], i[2] # airport_code, airport_names

# ФИРМА САМОЛЕТА (aircraft_code, model)
def Aircraft_code_model():
    aircraft_name = random.choice(["Airbus 320", "Boeing 737", "Boeing 777",
                               "Airbus 330", "Boeing 747", "Boeing 767"])
    index = aircraft_name.find(" ")
    model = aircraft_name[:index]
    aircraft_code = aircraft_name[index+1:]
    return aircraft_code, model

# НОМЕР БИЛЕТА (ticket_no)
def Ticket_no():
    ticket_no0 = ''.join(random.choice(string.digits) for _ in range(12))
    return ticket_no0[6:] + "-" + ticket_no0[:6]

# НОМЕР ПОЛЕТА (flight_no)
def Flight_no():
    return ''.join(random.choice(string.digits) for _ in range(3))

# АЙДИ ПОЛЕТА (flight_id)
def Flight_id():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + " " + Flight_no()


# ИТОГОВАЯ ЦЕНА (amount)
def Amount(range1, fare_conditions):
    RATE = ((7918, 1100, "Эконом"), (9897, 1400, "Комфорт"),
        (19795, 2050, "Бизнес"), (28568, 3400, "Первый класс"))
    for i in range(len(RATE)):
        if RATE[i][2] == fare_conditions:
            sum1 = RATE[i][1] 
            sum2 = RATE[i][0] 
    return round((int(range1) * (sum2/1000)), 2) + sum1

# ПОСАДОЧНЫЙ НОМЕР (boarding_no)
def Boarding_no():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

# МЕСТО (seat_no)
def Seat_no():
    return ''.join(random.choice(string.digits) for _ in range(2))\
    + ''.join(random.choice(string.ascii_uppercase) for _ in range(1))

def Passenger_id():
    return ''.join(random.choice(string.digits) for _ in range(20))