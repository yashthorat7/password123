import os
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
import hashlib
import base64
from cryptography.fernet import Fernet

console = Console()
load_dotenv()


# stores the encrypted password
def StoreData(website, username, password):
    website = website if website else 'N/A'
    username = username if username else 'N/A'

    entry = f'{website}\t{username}\t{password.decode()}\n'
    with open('./data/password.enc', 'a') as file:
        file.write(entry)
    file.close()


# master key to 32byte url converter
def getFernetKey(key):
    hashed = hashlib.pbkdf2_hmac('sha256', key.encode(), b'', 100000, dklen=32)
    fernetKey = base64.urlsafe_b64encode(hashed)

    return fernetKey

# uses cryptography to encrypt the password
def EncryptPassword(password):
    key = os.getenv('MASTER_KEY')
    fernetKey = getFernetKey(key)
    cipher = Fernet(fernetKey)
    encryptedPassword = cipher.encrypt(password.encode())

    return encryptedPassword

# uses cryptography to decrypt the password
def DecryptPassword(password, key):
    fernetKey = getFernetKey(key)
    cipher = Fernet(fernetKey)
    decryptedPassword = ''

    try:
        decryptedPassword = cipher.decrypt(password).decode()
    except:
        decryptedPassword = 'Error!'

    return decryptedPassword


# called right after password generation
def SavePassword(password=''):
    action = 'saved'
    console.print(Text('Enter the Website ', style='purple') + Text(f'(optional)', style='blue') + Text(': ', style='purple'), end='')
    website = input()
    console.print(Text('Enter the Username ', style='purple') + Text(f'(optional)', style='blue') + Text(': ', style='purple'), end='')
    username = input()

    #if the request is not coming right after generation
    if password == '':
        action = 'added'
        console.print(Text('Enter the Password: ', style='purple'), end='')
        password = input()

    encryptedPassword = EncryptPassword(password)
    StoreData(website, username, encryptedPassword)


    console.print(Text(f'\nPassword {action} successfully...\n', style='yellow'))