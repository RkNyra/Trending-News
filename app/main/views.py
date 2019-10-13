from flask import render_template
from app import app
from requests import get_news

#Views

#Homepage
@app.route('/')
def index():
  '''
  View home page function that returns the index/home page and its data.
  '''
  
  #Getting news_updates
  updates = get_news('updates')
  print(updates)
  
  title = 'Trending News'
  NewsLink = 'News'
  return render_template('index.html', title = title, NewsLink = NewsLink)


#News-Article Page/ Article ID - Navigate to specific news article
@app.route('/news/<int:news_id>')
def news(news_id):
  '''
  View news page function that returns the news article page with the respective news.
  '''
  title = 'Trending News'
  return render_template('news.html', title = title, id = news_id)
