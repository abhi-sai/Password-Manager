from Database import checkCredentials, setUser, addUser
from passwordGenerator import setKey

def loginAuthentication():
    print("Do you want to : ")
    print("1) Log in")
    print("2) Sign up")
    choice = input("Enter option: ")

    if choice == '1':
        return login()

    elif choice == '2':
        return addNewUser()

    else:
        print("Enter correct option")
        loginAuthentication()


def login():
    user = input("Enter Username : ")
    password = input("Enter Password : ")

    if checkCredentials(user, password) is False:
        print("Invalid username or password")
        c = input("Do you want to try again? (Y/N) : ")
        if c == 'Y' or c == 'y':
            return login()
        else:
            return False
    else:
        setUser(user, password)
        setKey(password)
        return True


def addNewUser():
    user = input("Enter Username : ")
    password = input("Enter Password : ")

    if (addUser(user, password)):
        setUser(user, password)
        setKey(password)
        return True
    else:
        print("User already exists")
        choice = input("Would you like to sign in? (Y/N)")
        if (choice == 'Y' or choice == 'y'):
            return login()
        else:
            i = input("Would you like to create an account? (Y/N)")
            if i == 'Y' or i == 'y':
                addNewUser()
            else:
                return False
