from app import app
import urllib.request,json
from .models import news_article, news_source

Article = news_article.Article
Source = news_source.Source

#Get the news api key
api_key = app.config['NEWS_API_KEY']

#Get the news base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(updates):
  '''
  Function that gets the json response to the url request
  '''
  get_news_url = base_url.format(updates,api_key)
  
  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)
    
    news_articles = None
    
    if get_news_response['articles']:
      news_articles_list = get_news_response['articles']
      
      news_articles = process_articles(news_articles_list)

  return news_articles