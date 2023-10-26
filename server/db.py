# This file will handle the connection to the database

# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime

class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                            password='pass',
                                            host='localhost',
                                            port=3306,
                                            database='bakery')
        self.cursor = self.conn.cursor()

    def get_goods_from_db(self):
        query = ("""SELECT * FROM goods""")
        self.cursor.execute(query,)
        returned_data = self.cursor.fetchall()
        return returned_data
    
    def get_unique_goods_from_db(self):
        query = ("""SELECT DISTINCT good_name FROM goods""")
        self.cursor.execute(query,)
        unique_good_names = self.cursor.fetchall()
        return unique_good_names
    
    def enter_sold_goods_into_database(self, post_data):
        self._SQL = """insert into goods
        (good_name, amount, date_stamp)
        values
        (%s, %s, %s)"""
        self.cursor.execute(self._SQL, (post_data['item'],
                            post_data['amount'], post_data['date']))
        self.conn.commit()
        item_inserted = True
        return item_inserted



db = Connection() 
db.get_goods_from_db()