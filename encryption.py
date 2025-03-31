from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from secrets import token_bytes
from base64 import urlsafe_b64encode

def derive_key(entry:str, salt):
    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=2,
        lanes=2,
        memory_cost=64*1024,
        ad=None,
        secret=None
    )
    return kdf.derive(entry.encode())


def verify_password(entry:str, salt):

    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=2,
        lanes=4,
        memory_cost=64*1024,
        ad=None,
        secret=None
    )
    return kdf.verify(derive_key(entry, salt), 'this needs to be ')

def encrypt_data(password:str, data:str, salt:bytes):
    key = urlsafe_b64encode(derive_key(password, salt))
    f = Fernet(key)
    return f.encrypt(data.encode())
