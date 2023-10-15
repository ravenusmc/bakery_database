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
        row = self.cursor.fetchall()
        print(row)

db = Connection() 
db.get_goods_from_db()