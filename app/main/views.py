from flask import render_template, redirect, request, url_for
from . import main
# from app import app
from ..requests import get_news, get_articles
from ..models import news_source, news_article

#Views

#Homepage
# @app.route('/')
@main.route('/')
def index():
  '''
  View home page function that returns the index/home page and its data.
  '''
  
  #Getting news sources
  news_names = get_news()
  print(news_names)
  
  # <link rel = "shortcut icon" href = "{{ url_for('static', filename='TrendingNewsFavicon.ico') }}" >

  title = 'Trending News'
  NewsLink = 'News'
  return render_template('index.html', title=title, NewsLink=NewsLink, name=news_names)


#News-Article Page/ Article ID - Navigate to specific news article
# @app.route('/news/<id>')
@main.route('/news/<id>')
def articles(id):
  '''
  View news page function that returns the news article page with the respective news.
  '''
  # Getting news articles
  articles_names = get_articles(id)
  print(articles_names)
  
  title = 'Trending News'
  return render_template('news.html', title = title, newsart = articles_names)
