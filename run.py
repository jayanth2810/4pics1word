__author__ = 'jayanthvenkataraman'

import os

from app import app

port = int(os.environ.get('PORT', 5000))  # for taking Heroku's PORT environment variable
app.run(host='https://***.herokuapp.com:443', port=port, debug=False)
