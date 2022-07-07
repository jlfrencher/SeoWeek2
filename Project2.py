from pprint import pprint
import requests
import googlemaps
import os
import pandas as pd

# Setting up environment to conceal the api key
API_KEY = os.environ.get('MAPS_API_KEY')
map_client = googlemaps.Client(API_KEY)


def get_distance(starting_point, ending_point):
    location = map_client.distance_matrix(starting_point, ending_point)

    distance_in_km = location['rows'][0]['elements'][0]['distance']['text']

    km_nochars = distance_in_km.replace(',', '')
    km_nochars = km_nochars.replace(' km', '')

    return int(km_nochars)
# Creating the database to store information
data = {'name': [],
    'email': [],
    'phone number': [],
    'item name': [],
    'address': [],
    'category':[]
    }
    
df = pd.DataFrame(data)


def determine_user_type():
    initial_input = input("Enter 'buy' if you want to see the list of items and 'sell' if you want to list an item to sell")
    if initial_input == 'sell' and len(df.index) == 0:
        initial_database()
    
    elif initial_input == 'sell' and len(df.index) != 0:
        add_to_database()


def initial_database():

    # Adding first seller's input/information into the dataframe
    global data
    name = input("Enter your name")
    data['name'].append(name) 

    email = input("Enter your email")
    data['email'].append(email) 

    phone_number = input("Enter your phone number without dashes")
    data['phone number'].append(phone_number)

    item_name = input("Enter the name of the item that you want to sell")
    data['item name'].append(item_name)

    address = input("Enter your address")
    data['address'].append(address)

    print("Electronics \nClothes \nFree \nSports equipment \nOther")
    category = input("Choose a category from the list above").lower()
    while category != 'clothes' and category != 'electronics' and category != 'free' and category != 'sports equipment' and category != 'other':
        category = input("Please enter a category from the list above").lower()
    data['category'].append(category) 

    global df
    df = df.append(data, ignore_index = True)
    print (df)

def add_to_database():
    new_data = {'name': [""],
    'email': [""],
    'phone number': [""],
    'item name': [""],
    'address': [""],
    'category':[""]
    }
    # Adding additional seller's input/information into the dataframe
    global data
    name = input("Enter your name")
    new_data['name'][0] = name

    email = input("Enter your email")
    new_data['email'][0] = email

    phone_number = input("Enter your phone number without dashes")
    new_data['phone number'][0] = phone_number

    item_name = input("Enter the name of the item that you want to sell")
    new_data['item name'][0] = item_name

    address = input("Enter your address")
    new_data['address'][0] = address

    print("Electronics \nClothes \nFree \nSports equipment \nOther")
    category = input("Choose a category from the list above").lower()
    while category != 'clothes' and category != 'electronics' and category != 'free' and category != 'sports equipment' and category != 'other':
        category = input("Please enter a category from the list above").lower()
    new_data['category'][0] = category

    global df
    df = df.append(new_data, ignore_index = True)
    print (df)

while True:
    determine_user_type()

print(get_distance('1311 39th st Des Moines Iowa', 
'7235 Kingsland Drive Memphis Tennessee'))

print(get_distance('1311 39th st Des Moines Iowa'
    ,'7235 Kingsland Drive Memphis Tennessee'))

