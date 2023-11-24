import api, connection
from flask import jsonify, request, Flask
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
#app.config("DEBUG") = True
CORS(app)

connection = mysql.connector.connect(user='adminserver',
                                     password='Contra12@34',
                                     host='UbuntuServer',
                                     database='appDelivery',
                                     port='3306')

mycursor = connection.cursor()
mycursor.execute("SELECT * FROM usuarios")

print(connection)

@app.route('/usuario', methods=['GET'])
def users():
    return jsonify()