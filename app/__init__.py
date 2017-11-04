__author__ = 'jayanthvenkataraman'

from flask import Flask
from flask_restplus import Api

app = Flask(__name__)

api = Api(app, version='1.0', title='4 Pic 1 Word Clue Generator',
          description='4 Pic 1 Word Clue Generator')

from app import views
