from geopy.geocoders import Nominatim

def get_location(ip):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ip)
    return location.address