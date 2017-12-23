import sys
import pickle
import passwordGenerator


def main():
    action = sys.argv[1]

    assert action in ['create', 'get', 'edit', 'remove', 'list'], 'Action not recognized'

    checkFile()

    process(action)


def checkFile():
    try:
        file = open('data.pickle', 'r')
    except FileNotFoundError:
        file = open('data.pickle', 'w')
    file.close()


def process(action):
    if action == 'create' or action == 'edit':
        service = sys.argv[2]
        masterPass = sys.argv[3]
        create(service, masterPass)
    elif action == 'get':
        service = sys.argv[2]
        get(service)
    elif action == 'remove':
        service = sys.argv[2]
        remove(service)
    elif action == 'list':
        printAllPasswords()


def get(service):
    with open('data.pickle', 'rb') as f:
        try:
            data = pickle.load(f)
            print(data[service])
        except:
            print("Password not found")


def create(service, masterPass):
    data = getDictionary()
    data[service] = passwordGenerator.password(service, masterPass)
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
    data = getDictionary()
    if len(data) == 0:
        print("No Passwords Found")
    else:
        for key, value in data.items(): print(key + " " + value)


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


if __name__ == '__main__':
    main()
