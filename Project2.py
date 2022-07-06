from pprint import pprint
import requests
import googlemaps

map_client = googlemaps.Client(API_KEY)

location = map_client.distance_matrix('1311 39th st Des Moines Iowa', '7235 Kingsland Drive Memphis Tennessee')

print(location)

"""
origin = '1311 39th street Des Moines Iowa'
destination = '6222 frankline ave Des Moines Iowa'

url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key=' + API_KEY
"""

"""
"""