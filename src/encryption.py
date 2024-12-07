import os
from rich.console import Console
from cryptography.fernet import Fernet

def StoreData(website, username, password):
    website = website if website else 'N/A'
    username = username if username else 'N/A'

    entry = f'{website}-{username}-{password.decode()}\n'
    with open('./data/password.enc', 'a') as file:
        file.write(entry)


def EncryptPassword(password):
    key = os.getenv('MASTER_KEY')
    cipher = Fernet(key)
    encryptPassword = cipher.encrypt(password.encode())

    return encryptPassword


# called right after password generation
def SavePassword(password):
    website = input('Enter the website (optional): ')
    username = input('Enter the username (optional): ')
    
    encryptedPassword = EncryptPassword(password)
    
    StoreData(website, username, encryptedPassword)

    print('\nPassword saved successfully...\n')