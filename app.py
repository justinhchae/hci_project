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