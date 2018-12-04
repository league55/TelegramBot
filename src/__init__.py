import os

from flask import Flask

MONGO_URL = os.environ.get('MONGO_URL')

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URL
