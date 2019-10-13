from flask import Flask
from config import DevConfig

#Initializing the application
app = Flask(__name__)

#Configuration set-up
app.config.from_object(DevConfig)

from main import views
