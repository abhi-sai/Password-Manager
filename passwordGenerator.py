from hashlib import sha256

ALPHABET = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')

SECRET_KEY = 'p4k_zA'


def get_hexdigest(salt, password):
    return sha256((salt + password).encode('utf-8')).hexdigest()


def make_password(plaintext, service):
    salt = get_hexdigest(SECRET_KEY, service)[:20]
    hsh = get_hexdigest(salt, plaintext)
    return ''.join((salt, hsh))


def password(plaintext, service, length=10, alphabet=ALPHABET):
    raw_hexdigest = make_password(plaintext, service)

    num = int(raw_hexdigest, 16)

    num_chars = len(alphabet)

    chars = []
    while len(chars) < length:
        num, idx = divmod(num, num_chars)
        chars.append(alphabet[idx])

    return ''.join(chars)
