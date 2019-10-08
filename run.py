#!/usr/bin/env python3.6
from credentials import Credentials
from user import User
import random


def create_credentials(fname, lname, phone, email, username, account, password):
    '''
    Function to create a new contact
    '''
    new_credentials = Credentials(
        fname, lname, phone, email, username, account, password)
    return new_credentials


