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


def save_credentials(credentials):
    '''
    Function to save contact
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete credentilas
    '''
    credentials.delete_credentials()


def find_credentials(acc):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_credentials_by_acc(acc)


def check_existing_user(pass_word):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exists(pass_word)


def check_existing_credentials(acc):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.credentials_exists(acc)


def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()


def main():

 while True:

                    print(
                        "Hello Welcome to your PasswordLocker app.Explore your accounts and feel free to add another. What is your name?")
                    print("What is your name\n")
                    user_name = input()

                    print(f"Habari yako {user_name}. what would you like to do?")
                    print('\n')

                    print("\n Login")
                    print("="*100)

                   

                    print("=" * 100)
                    u_name = input()

                    print("\n Password.....")
                    print("+" * 100)
                    pass_word = input()
                   