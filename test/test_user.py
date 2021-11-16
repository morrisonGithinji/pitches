from app.models import  User
from app import db
import unittest

class UserModelTest(unittest.TestCase):

  def setUp(self):
    self.user_ebay = User(username ='morriosn', email = 'morrison.githinji@student.moringaschool.com', pass_secure = '12345')
    
    
    
  def test_check_instance(self):
      self.assertEquals(self.user_ebay.username, 'morrison')
      self.assertEquals(self.user_ebay.email,'morrison.githinji@student.moringaschool.com')
      self.assertEquals(self.user_ebay.pass_secure,'12345')
    
  def test_password_setter(self):
          self.assertTrue(self.user_ebay.pass_secure is not None)

  def test_no_access_password(self):
              with self.assertRaises(AttributeError):
                  self.user_ebay.password

  def test_password_verification(self):
              self.assertTrue(self.user_ebay.verify_password('12345')) 