from cryptography.fernet import Fernet
from .encrypter import get_fernet_key

def decrypt(password, key):
    fernet_key = get_fernet_key(key)
    cipher = Fernet(fernet_key)
    try:
        return cipher.decrypt(password).decode()
    except Exception:
        return '[Error]'