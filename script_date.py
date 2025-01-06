from datetime import datetime, timedelta
import random

def Data_time(times, formatted_date):
    global today, book_date
    book_date = "n"
    today = datetime.now()

    year = int("20" + str(formatted_date)[-2:])
    month = int(str(formatted_date)[3:5])
    day = int(str(formatted_date)[:2])

    n1 = random.choice([i for i in range(0, 51, 10)])
    list_time_fly = datetime(year, month, day, random.randint(0, 23), n1, 0)
    last_time = list_time_fly
    date1 = (last_time.strftime('%d.%m.%Y %H:%M'))
    
    hour = int(last_time.strftime('%H'))
    minute = int(last_time.strftime('%M'))
    
    today = datetime(year, month, day, hour, minute) + timedelta(minutes=times) 
    date2 = (today.strftime('%d.%m.%Y %H:%M'))

    return date1, date2



