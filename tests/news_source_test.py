import unittest
from app import models

Source = models.news_source.Source

class SourceTest(unittest.TestCase):
  '''
  Test class to test the behavior of the Source class
  '''

  def setUp(self):
    '''
    Set up method that will run before every News Source test
    '''
    
    self.new_news_source = Source('id','name','description','url','category','country')
    
    def _test_instance(self):
      self.assertTrue(isinstance(self.new_news_source, Source))
  

if __name__ == '__main__':
  unittest.main()
