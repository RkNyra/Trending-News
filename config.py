import os

#Parent/General Configurations
class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL='https://newsapi.org/v2/sources?apikey={}'
  ARTICLE_API_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
  
  NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
  
  

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


config_options = {
  'development':DevConfig,
  'production':ProdConfig
}