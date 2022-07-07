from pprint import pprint
import requests
import googlemaps
import os
import pandas as pd
import sqlalchemy as db

# Setting up environment to conceal the api key
API_KEY = os.environ.get('MAPS_API_KEY')
map_client = googlemaps.Client(API_KEY)


def get_distance(starting_point, ending_point):
    location = map_client.distance_matrix(starting_point, ending_point)

    distance_in_km = location['rows'][0]['elements'][0]['distance']['text']

    km_nochars = distance_in_km.replace(',', '')
    km_nochars = km_nochars.replace(' km', '')

    return int(km_nochars)


sections = ['name', 'email', 'phone number', 'item name', 'address', 'category']
df = pd.DataFrame(columns=sections)


def determine_user_type():
    initial_input = input("Enter 'buy' if you want to see the list of items and 'sell' if you want to list an item to sell")
    if initial_input == 'sell':
        add_to_database()
    

def add_to_database():
    new_data = {'name': [""],
    'email': [""],
    'phone number': [""],
    'item name': [""],
    'address': [""],
    'category':[""]
    }
    # Adding additional seller's input/information into the dataframe
    global df
    name = input("Enter your name")

    email = input("Enter your email")

    phone_number = input("Enter your phone number without dashes")

    item_name = input("Enter the name of the item that you want to sell")

    address = input("Enter your address")

    print("Electronics \nClothes \nFree \nSports equipment \nOther")
    category = input("Choose a category from the list above").lower()
    while category != 'clothes' and category != 'electronics' and category != 'free' and category != 'sports equipment' and category != 'other':
        category = input("Please enter a category from the list above").lower()

    global sections
    user_info_list = [name, email, phone_number, item_name, address, category]
    df2 = pd.DataFrame([user_info_list], columns = sections)
    df = df.append(df2, ignore_index = True)
    print(df)


    engine = db.create_engine('sqlite:///df.db', echo = False)
    sql_table = df.to_sql('Seller_Data', con = engine, if_exists = 'replace', index = False)
    print(engine.execute("SELECT * FROM Seller_Data").fetchall())


if __name__ == '__main__':
    while True:
        determine_user_type()
