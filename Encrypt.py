import base64
from Crypto.Cipher import AES
from Crypto import Random
from hashlib import sha256


def encrypt(password, key):
    password = pad(password)
    iv456 = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv456)
    return base64.b64encode(iv456 + cipher.encrypt(password)).decode('utf-8')


def pad(p):
    length = 32
    return p + (length - len(p) % length) * chr(length - len(p) % length)


def decrypt(encrypted, key):
    encrypted = base64.b64decode(encrypted)
    iv456 = encrypted[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv456)
    return unpad(cipher.decrypt(encrypted[AES.block_size:])).decode('utf-8')


def unpad(p):
    return p[:-ord(p[len(p) - 1:])]


# For testing encryption
if __name__ == '__main__':
    password = input("Enter Password: ")
    key = sha256('p4k_zA'.encode()).digest()
    enc = encrypt(password, key)
    print(enc)
    print(decrypt(enc, key))