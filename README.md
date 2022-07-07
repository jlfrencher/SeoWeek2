# SeoWeek2
#### Setup Instructions
* pip install googlemaps
* You will need to assign an environmental variable called 'MAPS_API_KEY' to your Google API key.

#### How to Run
* First input if you are a buyer or a seller.
* Sellers input data, following prompts, about themselves and what they are selling/giving away.
* This gets added to the list of things being sold to be viewed by the buyer.

#### Overview of Code
* Our code creates and adds to a database from the user input of a buyer.
* We use pandas for the creation and altering of the database.
* Using sqlalchemy we convert the pandas dataframe to a table.