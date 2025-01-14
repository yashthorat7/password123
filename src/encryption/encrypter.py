import base64
import hashlib
from cryptography.fernet import Fernet

def get_fernet_key(master_key):
    """Generates Fernet key from master key using SHA-256."""
    key = hashlib.sha256(master_key.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt(password, master_key):
    """Encrypts password using Fernet symmetric encryption."""
    fernet_key = get_fernet_key(master_key)
    cipher = Fernet(fernet_key)
    return cipher.encrypt(password.encode())

