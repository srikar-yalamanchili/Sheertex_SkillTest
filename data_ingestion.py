# Importing all the required libraries
import requests
import sqlalchemy
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData, String, insert
import os
from datetime import datetime

# Create a SQLite Database if not exist
engine = create_engine('sqlite:///datawarehouse.db', echo=False)

req = requests.get('http://127.0.0.1:5000/api/orders/1/31')
data = req.json()  # Store the data in Json format
if data:
    orders_data = req.json()['orders']
    for i in range(0, len(orders_data)):
        orders = {'id': orders_data[i][0], 'created_at': orders_data[i][1], 'state': orders_data[i][3],
                  'total': orders_data[i][9], 'currency': orders_data[i][5]}
        order_items = {'order_id': orders_data[i][0], 'sku': orders_data[i][7], 'quantity': orders_data[i][8],
                       'price': orders_data[i][4]}
        conn = sqlite3.connect('datawarehouse.db', check_same_thread=False)  # connect to the datawarehouse db
        orders_table = """CREATE TABLE IF NOT EXISTS orders (id int,created_at text,state text,total int,currency text, ingested_at datetime);"""  # Create a table if not exits
        order_items_table = """CREATE TABLE IF NOT EXISTS order_items (order_id int,sku text,quantity text,price int, ingested_at datetime);"""  # Create a table if not exits
        cur = conn.cursor()  # To allow python code to execute sql commands in the database session
        table_orders = cur.execute(orders_table)  # Execute the orders table query
        table_order_items = cur.execute(order_items_table)  # Execute the order items table query
        ingest_orders = cur.execute("INSERT INTO orders(id,created_at,state,total,currency, ingested_at) VALUES (?,?,?,?,?, datetime('now', 'localtime'))", (
            orders['id'], orders['created_at'], orders['state'], orders['total'], orders['currency']))
        ingest_order_items = cur.execute("INSERT INTO order_items(order_id,sku,quantity,price, ingested_at) VALUES (?,?,?,?, datetime('now', 'localtime'))", (
            order_items['order_id'], order_items['sku'], order_items['quantity'], order_items['price']))
        conn.commit()  # Save the changes.
    print('orders and order_items are updated in datawarehouse.db at',
          datetime.now().strftime("%d/%m/%Y %H:%M:%S"))  # once it is executed, print the status.
else:
    print("Data is not availab  le at the end point, please check the endpoint and try again.")
