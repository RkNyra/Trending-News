from app import app
import urllib.request,json
from .models import news_article, news_source

Article = news_article.Article
Source = news_source.Source

#Get the news api key
apikey = app.config['NEWS_API_KEY']

#Get the news base url
base_url = app.config["NEWS_API_BASE_URL"]

#Get the articles base url
article_base_url = app.config["ARTICLE_API_BASE_URL"]


def get_news():
  '''
  Function that gets the json response to the url request
  '''
  get_news_url = base_url.format(apikey)
  
  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)
    
    news_sources = None
    
    if get_news_response['sources']:
      news_sources_list = get_news_response['sources']
      
      news_sources = process_sources(news_sources_list)

  return news_sources



def process_sources(source_list):
  '''
  Function that processes the news sources and transforms them to a list of objects
  
  
  Args:
    source_list: A list of dictionaries that contain news source details
  
  Returns:
    news_sources: A list of news source objects
  '''
  
  news_sources = []
  for source in source_list:
    id = source.get('id')
    name = source.get('name')
    description = source.get('description')
    url = source.get('url')
    category = source.get('category')
    country = source.get('country')
  
    if name:
      new_source_object = Source(id, name, description, url, category, country)
      news_sources.append(new_source_object)
    
  return news_sources


# Getting the news article(s)
def get_articles(id):
  '''
  Function that gets the json articles response to the url request
  '''
  get_articles_url = article_base_url.format(id, apikey)

  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)

    news_articles = None

    if get_articles_response['articles']:
      news_articles_list = get_articles_response['articles']

      news_articles = process_articles(news_articles_list)

  return news_articles


def process_articles(articles_list):
  '''
  Function that processes the news articles and transforms them to a list of objects
  
  
  Args:
    articles_list: A list of dictionaries that contain news article details
  
  Returns:
    news_articles: A list of news article objects
  '''

  news_articles = []
  for article in articles_list:
    urlToImage = article.get('urlToImage')
    description = article.get('description')
    publishedAt = article.get('publishedAt')
    url = article.get('url')
   

    if url:
      new_article_object = Article(urlToImage, description, publishedAt, url)
      news_articles.append(new_article_object)

  return news_articles
