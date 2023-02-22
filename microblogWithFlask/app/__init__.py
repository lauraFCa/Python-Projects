from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

from app import routes # app = directory

'''
The bottom import is a workaround to circular imports, a common problem with Flask applications.
You are going to see that the routes module needs to import the app variable defined in this script
'''
