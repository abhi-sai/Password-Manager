from pymongo import MongoClient

with open('auth', 'r') as f:
    mongoURL = f.read()

client = MongoClient(mongoURL)
db = client.passBook
collection = db.mainCollection
userName = None
key = None


def addUser(user, password):
    if (checkExists(user)):
        return False
    else:
        collection.insert_one({'User': user,
                               'Password': password,
                               'Data': []
                               })
        return True


def addData(service, user, password):
    if (checkService(service)):
        return False
    else:
        collection.find_one_and_update({'User': userName},
                                       {'$push': {
                                           'Data': {
                                               'Service': service,
                                               'ServiceUser': user,
                                               'ServicePass': password
                                           }
                                       }})
        return True


def getData(service):
    serviceData = getServices()
    if serviceData:
        for s in serviceData:
            if s['Service'] == service:
                print("Username: " + s['ServiceUser'])
                print("Password: " + s['ServicePass'])
                return True

    return False


def removeService(service):
    serviceData = getServices()
    if serviceData:
        for i in range(len(serviceData)):
            if serviceData[i]['Service'] == service:
                del (serviceData[i])
                collection.find_one_and_update({'User': userName},
                                               {'$set': {'Data': serviceData}})
                return True
    return False


def editService(service):
    serviceData = getServices()

    if serviceData:
        newUser = input("Enter new username (Leave it empty if its unchanged): ")
        newPass = input("Enter new password (Leave it empty if its unchanged): ")
        for i in range(len(serviceData)):
            if serviceData[i]['Service'] == service:
                if newUser:
                    serviceData[i]['ServiceUser'] = newUser
                if newPass:
                    serviceData[i]['ServicePass'] = newPass
                collection.find_one_and_update({'User': userName},
                                               {'$set': {'Data': serviceData}})
                return True
    return False


def setUser(user, password):
    global userName
    global key
    userName = user
    key = password


def checkCredentials(user, password):
    if collection.find_one({"User": user, 'Password': password}) is not None:
        return True
    else:
        return False


def checkExists(user):
    if collection.find_one({'User': user}) is None:
        return False
    else:
        return True


def checkService(service):
    serviceArray = getServices()
    if serviceArray:
        for s in serviceArray:
            if s['Service'] == service:
                return True

    return False


def getServices():
    array = collection.find_one({'User': userName})
    serviceArray = array['Data']
    return serviceArray
