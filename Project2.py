from pprint import pprint
import re
import requests
import googlemaps

map_client = googlemaps.Client(API_KEY)

def get_distance(starting_point, ending_point):
    location = map_client.distance_matrix(starting_point, ending_point)

    distance_in_km = location['rows'][0]['elements'][0]['distance']['text']

    km_nochars = distance_in_km.replace(',', '')
    km_nochars = km_nochars.replace(' km', '')

    return int(km_nochars)

print(get_distance('1311 39th st Des Moines Iowa', '7235 Kingsland Drive Memphis Tennessee'))

"""
origin = '1311 39th street Des Moines Iowa'
destination = '6222 frankline ave Des Moines Iowa'

url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key=' + API_KEY
"""

"""
"""