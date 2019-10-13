from flask import render_template
from app import app

#Views

#Homepage
@app.route('/')
def index():
  '''
  View home page function that returns the index/home page and its data.
  '''
  NewsLink = 'News'
  return render_template('index.html', NewsLink = NewsLink)


#Article ID - Navigate to specific news article
@app.route('/news/<int:news_id>')
def news(news_id):
  '''
  View news page function that returns the news article page with the respective news.
  '''
  return render_template('news.html',id = news_id)