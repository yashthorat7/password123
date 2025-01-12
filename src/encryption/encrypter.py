import hashlib
import base64
from cryptography.fernet import Fernet

def get_fernet_key(key):
    hashed = hashlib.pbkdf2_hmac('sha256', key.encode(), b'', 100000, dklen=32)
    return base64.urlsafe_b64encode(hashed)

def encrypt(password, master_key):
    fernet_key = get_fernet_key(master_key)
    cipher = Fernet(fernet_key)
    encrypted_bytes = cipher.encrypt(password.encode())
    encrypted_bytes = encrypted_bytes.decode()
    return encrypted_bytes

