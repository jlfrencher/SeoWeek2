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
    print(location)

    distance_in_km = location['rows'][0]['elements'][0]['distance']['text']

    km_nochars = distance_in_km.replace(',', '')
    km_nochars = km_nochars.replace(' km', '')

    return int(km_nochars)


sections = ['name', 'email', 'phone number', 'item_name', 'address', 'category']
df = pd.DataFrame(columns=sections)


def determine_user_type():
    initial_input = input("Enter 'buy' if you want to see the list of items, 'sell' if you want to list an item to sell, or 'q' if you want to quit: ")
    if initial_input == 'sell':
        current_user_info = get_user_input()
        add_to_database(current_user_info)
    if initial_input == 'buy':
        display_database()
    if initial_input == 'q':
        quit()


def get_user_input():
    name = input("Enter your name: ")

    email = input("Enter your email: ")

    phone_number = input("Enter your phone number without dashes: ")

    item_name = input("Enter the name of the item that you want to sell: ")

    address = input("Enter your address: ")

    category = print_categories()
    user_info_list = [name, email, phone_number, item_name, address, category]
    return user_info_list


def add_to_database(user_list):
    # Adding additional seller's input/information into the dataframe
    global df
    global sections
    df2 = pd.DataFrame([user_list], columns = sections)
    df = df.append(df2, ignore_index = True)
    print(df)


    engine = db.create_engine('sqlite:///df.db', echo = False)
    sql_table = df.to_sql('Seller_Data', con = engine, if_exists = 'replace', index = False)
    print(engine.execute("SELECT * FROM Seller_Data").fetchall())


def display_database():
    engine = db.create_engine('sqlite:///df.db', echo = False)
    user_table = pd.read_sql_table(table_name="Seller_Data", con=engine)
    print(user_table)

    next_input = print_categories()
    #print(engine.execute("SELECT * FROM Seller_Data WHERE category = '" + next_input + "'").fetchall())
    global df
    df2 = df[df['category'].str.contains(next_input)]
    print(df2)
    item_wanted = input("Enter the name of the item you want")
    while (item_wanted in df['item_name'].unique()) == False:
        item_wanted = input("Please enter an item that exists in the list").lower()
    seller_address = engine.execute("SELECT address FROM Seller_Data WHERE item_name = '" + item_wanted + "'").fetchone()
    seller_address = seller_address[0]
    print(seller_address)
    buyer_address = input("Enter your address")
    location = map_client.distance_matrix(buyer_address, seller_address)

    distance_in_km = location['rows'][0]['elements'][0]['distance']['text']
    time = location['rows'][0]['elements'][0]['duration']['text']
    print(distance_in_km)
    print(time)

def print_categories():
    print("Categories:\nElectronics \nClothes \nFree \nSports equipment \nOther")
    next_input = input("What category would you like to buy from?: ")
    while next_input != 'clothes' and next_input != 'electronics' and next_input != 'free' and next_input != 'sports equipment' and next_input != 'other':
        next_input = input("Please enter a category from the list above").lower()
    return next_input


if __name__ == '__main__':
    while True:
        determine_user_type()
