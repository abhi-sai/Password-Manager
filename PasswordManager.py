import sys
import pickle
from hashlib import sha256

SECRET_KEY = 's3cr3t'


def main():
    action = sys.argv[1]

    assert action in ['create', 'get'], 'Action not recognized'

    process(action)


def process(action):
    if action == 'create':
        service = sys.argv[2]
        masterPass = sys.argv[3]
        create(service, masterPass)
    elif action == 'get':
        service = sys.argv[2]
        get(service)


def get(service):
    with open('data.pickle', 'rb') as f:
        try:
            data = pickle.load(f)
            print(data[service])
        except:
            print("Password not found")


def create(service, masterPass):
    with open('data.pickle', 'rb') as f:
        try:
            data = pickle.load(f)
        except:
            data = dict()

    data[service] = password(service, masterPass)

    with open('data.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def get_hexdigest(salt, password):
    return sha256((salt + password).encode('utf-8')).hexdigest()


def make_password(plaintext, service):
    salt = get_hexdigest(SECRET_KEY, service)[:20]
    hsh = get_hexdigest(salt, plaintext)
    return ''.join((salt, hsh))


ALPHABET = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')


def password(plaintext, service, length=10, alphabet=ALPHABET):
    raw_hexdigest = make_password(plaintext, service)

    # Convert the hexdigest into decimal
    num = int(raw_hexdigest, 16)

    # What base will we convert `num` into?
    num_chars = len(alphabet)

    # Build up the new password one "digit" at a time,
    # up to a certain length
    chars = []
    while len(chars) < length:
        num, idx = divmod(num, num_chars)
        chars.append(alphabet[idx])

    return ''.join(chars)


if __name__ == '__main__':
    main()
