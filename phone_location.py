
"""
 Phone number tracker

 Created by *Abdullah EL-Yamany*

 Channal Name => Simplilearn
 Link Video => https://youtu.be/DY4M9bAVyUc
"""

import phonenumbers
from phonenumbers import geocoder
import folium

number = "+xxxxxxxxxxxxx" # +CodeCountry PhoneNumber


check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

#-----------------------------------

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

#-----------------------------------

key = "xxxxxxxxxxxxxxxxxxxxxxxxxx" From =>  https://opencagedata.com/dashboard#geocoding > API Keys

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = (str(number_location))
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)


map_location = folium.Map(location = [lat, lng], zoom_start=9)
folium.Marker([lat, lng],popup=number_location).add_to(map_location)
map_location.save("myLocation.html")

