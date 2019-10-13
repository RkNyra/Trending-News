#Parent/General Configurations
class Config:
  '''
  General configuration parent class
  '''
  pass

#Production Configurations
class ProdConfig(Config):
  '''
  Production configuration child class
  
  Args:
    Config: The parent config class with the General configuration settings
  '''
  pass

#Dev Configurations
class DevConfig(Config):
  '''
  Dev configuration child class
  
  Args:
    Config: The parent config class with the General configuration settings
  '''
  DEBUG = True