from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I created for the project
from db import *


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/fetchDatabaseData', methods=['GET', 'POST'])
def fetchDatabaseData():
    if request.method == 'POST':
        db = Connection()
        returned_data = db.get_goods_from_db()
        unique_good_names = db.get_unique_goods_from_db()
        data_holder = []
        data_holder.append(returned_data)
        data_holder.append(unique_good_names)
    return jsonify(data_holder)

@app.route('/submitSalesDataToDatabase', methods=['GET', 'POST'])
def submit_sales_data_to_database():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        item_inserted = db.enter_sold_goods_into_database(post_data)
    return jsonify(item_inserted)

if __name__ == '__main__':
    app.run()