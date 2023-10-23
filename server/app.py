from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I created for the project
from db import *


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# May need to get rid of methods here and only use post
@app.route('/submitSalesDataToDatabase', methods=['GET', 'POST'])
def submit_sales_data_to_database():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        item_inserted = db.enter_sold_goods_into_database(post_data)
    return jsonify(item_inserted)

if __name__ == '__main__':
    app.run()