# Importing all the libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# creating a server
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Function to create a database
def create_database():
    csv_file = 'data.csv'  # Data file to read
    engine = create_engine('sqlite:///sheertex.db', echo=False)  # Create a sqlite db
    with open(f'{csv_file}', 'r') as file:  # open the csv file
        data_df = pd.read_csv(f'{csv_file}',
                              dtype={'id': int, 'created_at': str, 'customer': str, 'state': str, 'price': int,
                                     'currency': str, 'items': str, 'sku': str, 'quantity': int, 'total': int}) #schema for the dataframe
        print(data_df, data_df.columns)
    data_df.to_sql('orders_data', con=engine, index=False, index_label=None,
                   if_exists='replace')  # Replace if exist and table is named orders_data
    conn = sqlite3.connect('sheertex.db', check_same_thread=False)  # connect to the DB
    return conn


# Calling create_database function
conn = create_database()
if not conn:  # Verifying whether db is created.
    raise RuntimeError("Cannot create DB")


@app.route('/api/orders/<string:start_date>/<string:end_date>',
           methods=['GET'])  # Using GET method to retreive the data
def get_orders(start_date, end_date):
    try:
        cur = conn.cursor()  # To allow python code to execute sql commands in the database session
        all_orders = cur.execute(
            "select * from orders_data where created_at BETWEEN  " + start_date + " AND " + end_date + "")  # Extracting the start_date and End_date from the api
        result = dict(orders=all_orders.fetchall())  # converting all_orders to dictionary type
        return result  # return the result
    except:  # To check if is not able to fetch the data from the API
        print("Cannot fetch the details from the API")


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
