__author__ = 'jayanthvenkataraman'

from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

app = Flask(__name__)

api = Api(app, version='1.0', title='4 Pic 1 Word Clue Generator',
          description='4 Pic 1 Word Clue Generator')

cors = CORS(app)

from app import views
