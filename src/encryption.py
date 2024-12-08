import os
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
from cryptography.fernet import Fernet

console = Console()
load_dotenv()


# stores the encrypted password
def StoreData(website, username, password):
    website = website if website else 'N/A'
    username = username if username else 'N/A'

    entry = f'{website}\t\t{username}\t\t{password.decode()}\n'
    with open('./data/password.enc', 'a') as file:
        file.write(entry)
    file.close()


# use cryptography to encrypt the password
def EncryptPassword(password):
    key = os.getenv('MASTER_KEY')
    cipher = Fernet(key)
    encryptPassword = cipher.encrypt(password.encode())

    return encryptPassword


# called right after password generation
def SavePassword(password):
    console.print(Text('Enter the Website ', style='purple') + Text(f'(optional)', style='blue') + Text(': ', style='purple'), end='')
    website = input()
    console.print(Text('Enter the Username ', style='purple') + Text(f'(optional)', style='blue') + Text(': ', style='purple'), end='')
    username = input()

    encryptedPassword = EncryptPassword(password)
    
    StoreData(website, username, encryptedPassword)

    console.print(Text('\nPassword saved successfully...\n', style='yellow'))