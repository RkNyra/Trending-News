from flask import render_template
from app import app

#Views
@app.route('/')
def index():
  '''
  View home page function that returns the index/home page and its data.
  '''
  NewsLink = 'News'
  return render_template('index.html', NewsLink = NewsLink)