import pyperclip
import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
 def setUp(self):
    self.new_credentials = Credentials("maina001" ,"facebook","karobia", "maina", "0724550408","karobiamaina81@gamil.com", "maich" )
  
 def test_init(self):
    self.assertEqual(self.new_credentials.current_password, "maina001")
    self.assertEqual(self.new_credentials.account, "facebook")
    self.assertEqual(self.new_credentials.first_name, "karobia")
    self.assertEqual(self.new_credentials.last_name, "maina")
    self.assertEqual(self.new_credentials.phone_number, "0724550408")
    self.assertEqual(self.new_credentials.email_address, "karobiamaina81@gmail.com")
    self.assertEqual(self.new_credentials.username, "maich")
 
 def test_save_credentials(self):
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_details), 1)

 def test_save_multiple_credentials(self):
    self.new_credentials.save_credentials()
    test_credentials = Credentials("maina001" ,"facebook","karobia", "maina", "0724550408","karobiamaina81@gamil.com", "maich")
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_details), 2)

 def tearDown(self):
     Credentials.credentials_details = []

 def test_credentials_exists(self):
      self.new_credentials.save_credentials()
      test_credentials = Credentials("maina001" ,"facebook","karobia", "maina", "0724550408","karobiamaina81@gamil.com", "maich")
      test_credentials.save_credentials()

      credentials_exists = Credentials.credentials_exists("0712345678")
      self.assertTrue(credentials_exists)

 def test_display_all_credentials(self):
      self.assertEqual(Credentials.display_credentials(), Credentials.credentials_details)
 def test_copy_email_address(self):

      self.new_credentials.save_credentials()
      Credentials.copy_email_address("0724550408")

      self.assertEqual(self.new_credentials.email_address,pyperclip.paste())
      
if __name__ == '__main__':
      unittest.main()
