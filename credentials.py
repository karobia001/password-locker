class Credentials:
    credentials_details = []
    def __init__(self, current_password, account, first_name, last_name, phone_number, email_address, username):
        self.account = account
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.username = username
        self.current_password = current_password

    def save_credentials(self):
        Credentials.credentials_details.append(self)

    def tearDown(self):
        Credentials.credentials_details = []
   
    @classmethod
    def find_credentials_by_acc(cls, acc):
        for credentials in cls.credentials_details:
            if credentials.account == acc:
                return credentials

    @classmethod
    def credentials_exists(cls, acc):
        for credentials in cls.credentials_details:
            if credentials.account == acc:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        return cls.credentials_details
        