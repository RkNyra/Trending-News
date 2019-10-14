from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig

#Initializing the application
app = Flask(__name__,instance_relative_config = True)

#Configuration set-up
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initialize Flask Extensions
bootstrap = Bootstrap(app)

from .main import views
from .main import errors
