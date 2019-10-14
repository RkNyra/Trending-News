from flask import render_template, url_for
from app import app
from ..requests import get_news

#Views

#Homepage
@app.route('/')
def index():
  '''
  View home page function that returns the index/home page and its data.
  '''
  
  #Getting news names
  news_names = get_news()
  print(news_names)
  
  # <link rel = "shortcut icon" href = "{{ url_for('static', filename='TrendingNewsFavicon.ico') }}" >

  title = 'Trending News'
  NewsLink = 'News'
  return render_template('index.html', title=title, NewsLink=NewsLink, name=news_names)


#News-Article Page/ Article ID - Navigate to specific news article
@app.route('/news/<id>')
def news(id):
  '''
  View news page function that returns the news article page with the respective news.
  '''
  title = 'Trending News'
  return render_template('news.html', title = title, id = id)
