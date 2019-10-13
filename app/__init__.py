from flask import Flask
from config import DevConfig

#Initializing the application
app = Flask(__name__,instance_relative_config = True)

#Configuration set-up
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from .main import views
