class Article:
  '''
  Article class to define News Article Objects
  '''
  def __init__(self,urlToImage,description,publishedAt,url):
    self.urlToImage = urlToImage
    self.description = description
    self.publishedAt = publishedAt
    self.url = url
  