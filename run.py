__author__ = 'jayanthvenkataraman'

import os

from app import app

port = int(os.environ.get('PORT', 5000)) #for taking Heroku's PORT environment variable
app.run(host='0.0.0.0', port=port)
#app.run(host='0.0.0.0', port=8000, debug=False)
