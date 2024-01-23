from flask import Flask
from pymongo import MongoClient
import json
import random
app = Flask(__name__)

@app.route('/quote')
def quoting():

    # read tje json file with the quotes
    with open('quotes.json', 'r') as f:
        quotes = json.load(f)
    
    #get a random quote
    
    n = random.randint(1, len(quotes))
    quote = quotes[n]
    #display a quote from the mongodb collecion in a simple html format
    client = MongoClient()
    # Access the database
    db = client.quote_db

    # Get a random quote at each request
    quote = [doc for doc in db.quotes.aggregate([{ '$sample': { 'size': 1 } }])][0]
    client.close()

    # Display a title "quote of the day", the quote author and the quote
    return f'<h1>Quote of the Day</h1><h2>{quote["author"]}</h2><p>{quote["content"]}</p>'


if __name__ == '__main__':
    app.run()
    