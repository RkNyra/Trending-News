import unittest
from app import models
Article = news_article.Article
Source = news_source.Source

class ArticleTest(unittest.TestCase):
  '''
  Test class to test the behavior of the Article class
  '''
  def setUp(self):
    '''
    Set up method that will run before every Article test
    '''
    self.new_news_article = Article('https://images.cointelegraph.com/images/740_IGh0dHBzOi8vczMuY29pbnRlbGVncmFwaC5jb20vc3RvcmFnZS91cGxvYWRzL3ZpZXcvNjcyYjQ1MGJiMjQ4NjEzZDRmODlkNjBjZjM4Yjg1NTIuanBn.jpg', 'Combined with other technologies, Bitcoin will change how governments operate worldwide, according to billionaire investor Tim Draper', '2019-10-13T14:39:00Z','https://cointelegraph.com/news/bitcoin-will-end-the-reign-of-dictators-and-toll-trolls-says-tim-draper' )
    
    def test_instance(self):
      self.assertTrue(isinstance(self.new_news_article, Article))
    
    if __name__ == '__main__':
      unittest.main()
          