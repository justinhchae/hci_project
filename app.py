'''
To run on command line:
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
'''

from flask_restful import Api
from flask import Flask, request, Response
from flask_cors import CORS
from flask import render_template
import db

from dotenv import load_dotenv
load_dotenv()
import os
app = Flask(__name__)
CORS(app)
db.init_database_connection(app)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview/')
def make_page0():
    return render_template('overview.html')

@app.route('/temperament/')
def make_page1():
    return render_template('temperament.html')

@app.route('/thresholds/')
def make_page2():
    return render_template('thresholds.html')

if __name__ == "__main__":
    print('running!')
    app.run(debug=True)