import pickle
import passwordGenerator
from hashlib import sha256
from Encrypt import encrypt, decrypt

key = sha256('p4k_zA'.encode()).digest()


def checkFile():
    try:
        file = open('data.pickle', 'r')
    except FileNotFoundError:
        file = open('data.pickle', 'w')
    file.close()


def get(service):
    global key
    with open('data.pickle', 'rb') as f:
        try:
            data = pickle.load(f)
            print(decrypt(data[service], key))
        except:
            print("Password not found")


def create(service):
    global key
    data = getDictionary()
    password = passwordGenerator.password(service)
    data[service] = encrypt(password, key)
    print("Your password is: " + password)
    # print("Encrypted :" + data[service])
    writeToFile(data)


def add(service, password):
    global key
    data = getDictionary()
    data[service] = encrypt(password, key)
    writeToFile(data)


def remove(service):
    data = getDictionary()

    try:
        del data[service]
    except:
        print("Password not found")
        return

    writeToFile(data)


def printAllPasswords():
    global key
    data = getDictionary()
    if len(data) == 0:
        print("No Passwords Found")
    else:
        for service, password in data.items():
            print(service + " " + decrypt(password, key))


def getDictionary():
    with open('data.pickle', 'rb') as f:
        try:
            data = pickle.load(f)
        except:
            data = dict()
    return data


def writeToFile(data):
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
