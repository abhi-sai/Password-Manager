from pymongo import MongoClient
from hashlib import sha256
from Encrypt import encrypt, decrypt

with open('auth', 'r') as f:
    mongoURL = f.read()

client = MongoClient(mongoURL)
db = client.passBook
collection = db.mainCollection
userName = None
key = None


def addUser(user, password):
    if checkExists(user):
        return False
    else:
        collection.insert_one({'User': user,
                               'Password': sha256(password.encode()).digest(),
                               'Data': []
                               })
        return True


def addData(service, user, password):
    if getService(service) is not None:
        return False
    else:
        collection.find_one_and_update({'User': userName},
                                       {'$push': {
                                           'Data': {
                                               'Service': encrypt(service, key),
                                               'ServiceUser': encrypt(user, key),
                                               'ServicePass': encrypt(password, key)
                                           }
                                       }})
        return True


def getData(service):
    serviceData = getServicesList()
    if serviceData:
        for s in serviceData:
            if decrypt(s['Service'], key) == service:
                print("Username: " + decrypt(s['ServiceUser'], key))
                print("Password: " + decrypt(s['ServicePass'], key))
                return True

    return False


def removeService(service):
    enc_service = getService(service)
    if enc_service is not None:
        collection.update_one({'User': userName}, {'$pull': {'Data': {'Service': enc_service}}})
        return True
    else:
        return False


def editService(service):
    if removeService(service):
        newUser = input("Enter new username : ")
        newPass = input("Enter new password : ")
        addData(service, newUser, newPass)
    else:
        return False


def setUser(user, password):
    global userName
    global key
    userName = user
    key = sha256(password.encode()).digest()


def checkCredentials(user, password):
    pw = sha256(password.encode()).digest()
    if collection.find_one({"User": user, 'Password': pw}) is not None:
        return True
    else:
        return False


def checkExists(user):
    if collection.find_one({'User': user}) is None:
        return False
    else:
        return True


def getService(service):
    serviceArray = getServicesList()
    if serviceArray:
        for s in serviceArray:
            if decrypt(s['Service'], key) == service:
                return s['Service']

    return None


def getServicesList():
    array = collection.find_one({'User': userName})
    serviceArray = array['Data']
    return serviceArray
