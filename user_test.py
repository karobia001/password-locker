import pyperclip
import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("facebook","karobia", "maina", "0724550408","karobiamaina81@gmail.com", "maich", "maich001") # create user object

    def test_init(self):
        self.assertEqual(self.new_user.account, "facebook")
        self.assertEqual(self.new_user.first_name, "karobia")
        self.assertEqual(self.new_user.last_name, "maina")
        self.assertEqual(self.new_user.phone_number, "0724550408")
        self.assertEqual(self.new_user.email_address, "karobiamaina81@gmail.com")
        self.assertEqual(self.new_user.username, "maich")
        self.assertEqual(self.new_user.password, "maich001")
    
    
        
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_details), 1)
    
    def tearDown(self):
        User.user_details = []  
      
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("facebook","karobia", "maina", "0724550408","karobiamaina81@gamil.com", "maich", "maich001")
        test_user.save_user()
        self.assertEqual(len(User.user_details), 2)
     

    
    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("facebook","karobia", "maina", "0724550408","karobiamaina81@gamil.com", "maich", "maich001")
        test_user.save_user()

        user_exists = User.user_exists("0724550408")
        self.assertTrue(user_exists)
        
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_details
        '''
        User.user_details.remove(self)
        
        self.assertEqual(self.new_user.email_address,pyperclip.paste())
    
if __name__ == '__main__':
    unittest.main()

        