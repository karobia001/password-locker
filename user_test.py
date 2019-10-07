import unittest # import unittest module
from user import  Users # import the users class from User modul


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the users class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user  = Users ("facebook","maich","karobia001","maich") # create contact object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account_name,"facebook")
        self.assertEqual(self.new_user.username,"maich")
        self.assertEqual(self.new_user.email,"karobiamaina81@gmaol.com")
        self.assertEqual(self.new_user.password,"maich") 
    
    if __name__ == '__main__':
       unittest.main()
        