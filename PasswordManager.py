import passwordGenerator
from hashlib import sha256
from Encrypt import encrypt, decrypt
import Database

# key = sha256('p4k_zA'.encode()).digest()
key = Database.key


def get():
    global key
    service = input("Enter Service Name: ")
    if not Database.getData(service):
        print("Service not found")
        choice = input("Would you like to enter another Service? (Y/N) : ")
        if choice == 'Y' or choice == 'y':
            get()


def create():
    global key
    service = input("Enter Service Name: ")
    userName = input("Enter User Name: ")
    password = passwordGenerator.password(service)
    if Database.addData(service, userName, password) is False:
        choice = input("Service already exists. Would you like to add another service? (Y/N)")
        if choice == 'y' or choice == 'Y':
            create()
    else:
        print("Your password is: " + password)


def add():
    global key
    service = input("Enter Service Name: ")
    userName = input("Enter User Name: ")
    password = input("Enter Password: ")
    if Database.addData(service, userName, password) is False:
        choice = input("Service already exists. Would you like to add another service? (Y/N)")
        if choice == 'y' or choice == 'Y':
            add()


def remove():
    global key
    service = input("Enter Service Name: ")
    if Database.removeService(service) is False:
        print("Service not found")
        choice = input("Would you like to enter another Service? (Y/N) : ")
        if choice == 'Y' or choice == 'y':
            remove()

def edit():
    global key
    service = input("Enter Service Name: ")
    if Database.editService(service) is False:
        print("Service not found")
        choice = input("Would you like to enter another Service? (Y/N) : ")
        if choice == 'Y' or choice == 'y':
            edit()