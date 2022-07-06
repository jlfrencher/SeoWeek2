from pprint import pprint
import requests
import googlemaps
import os

API_KEY = os.environ.get('MAPS_API_KEY')
map_client = googlemaps.Client(API_KEY)


def get_distance(starting_point, ending_point):
    location = map_client.distance_matrix(starting_point, ending_point)

    distance_in_km = location['rows'][0]['elements'][0]['distance']['text']

    km_nochars = distance_in_km.replace(',', '')
    km_nochars = km_nochars.replace(' km', '')

    return int(km_nochars)


print(get_distance('1311 39th st Des Moines Iowa'
    ,'7235 Kingsland Drive Memphis Tennessee'))

