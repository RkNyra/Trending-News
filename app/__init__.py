from flask import Flask
from flask_bootstrap import Bootstrap
# from config import DevConfig
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__)
  

  # Creating the application configurations
  app.config.from_object(config_options[config_name])
  
  # Initialize flask extensions
  bootstrap.init_app(app)
  
  # Register the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  # Setting configurations
  from .requests import configure_request
  configure_request(app)

  #Initializing the application
  # app = Flask(__name__,instance_relative_config = True)

#Configuration set-up
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

#Initialize Flask Extensions
# bootstrap = Bootstrap(app)

  from .main import views
  from .main import errors

  return app
