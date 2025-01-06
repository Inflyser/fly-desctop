from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time

def Distance(flight_start, flight_end):
    
    def get_coordinates(city_name):
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(city_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None

    coordinates = get_coordinates(flight_start)

    if not coordinates:
        print(f"Не удалось найти координаты для города: {flight_start}")
        return None
    
    time.sleep(0.3)    

    coordinates1 = get_coordinates(flight_end)

    if not coordinates1:
        print(f"Не удалось найти координаты для города: {flight_end}")
        return None

    coords = (float(coordinates[0]), float(coordinates[1])) 
    coords1 = (float(coordinates1[0]), float(coordinates1[1])) 

    # Вычисление расстояния
    distance_km = geodesic(coords, coords1).kilometers

    print(f'Расстояние от {flight_start} до {flight_end} составляет: {distance_km:.2f} км')
    return round(distance_km, 2), (float(coordinates1[0]), float(coordinates1[1])) 
