import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://benjimallen_lab_10_db_user:TVjoaGbULbV2sqsq4NUqHrxFGuGB0q2P@dpg-cgmejdrk9u59cru9dk70-a/benjimallen_lab_10_db")
    conn.close()
    return 'Database Connection Successful'