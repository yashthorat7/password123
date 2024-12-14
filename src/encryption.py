import os
import hashlib
import base64
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
from cryptography.fernet import Fernet

console = Console()
load_dotenv()
PASSWORD_FILE = './data/passwords.enc'


def ReadPasswords():
    with open(PASSWORD_FILE, 'r') as file:
        return file.readlines()


def WritePasswords(lines):
    with open(PASSWORD_FILE, 'w') as file:
        file.writelines(lines)


def AppendPassword(entry):
    with open(PASSWORD_FILE, 'a') as file:
        file.write(entry)


def GetFernetKey(key):
    hashed = hashlib.pbkdf2_hmac('sha256', key.encode(), b'', 100000, dklen=32)
    return base64.urlsafe_b64encode(hashed)


def EncryptPassword(password, key):
    fernetKey = GetFernetKey(key)
    cipher = Fernet(fernetKey)
    return cipher.encrypt(password.encode())


def DecryptPassword(password, key):
    fernetKey = GetFernetKey(key)
    cipher = Fernet(fernetKey)
    try:
        return cipher.decrypt(password).decode()
    except Exception:
        return '[Error]'


def StorePasswordData(website, username, encryptedPassword):
    entry = f"{website}\t{username}\t{encryptedPassword.decode()}\n"
    AppendPassword(entry)


def SavePassword(key, password='', website='', username='', listing=False):
    try:
        if not listing:
            console.print(
                Text('Enter the Website: ', style='purple') + 
                Text('(optional)', style='blue') + 
                Text(': ', style='purple'), 
                end=''
            )
            website = input() or 'N/A'
            console.print(
                Text('Enter the Username: ', style='purple') + 
                Text('(optional)', style='blue') + 
                Text(': ', style='purple'), 
                end=''
            )
            username = input() or 'N/A'

        for _ in range(5):
            if not password:
                console.print(Text('Enter the Password: ', style='purple'), end='')
                password = input()
            if not password:
                console.print(Text('Password cannot be empty', style='red'))
            elif len(password) < 8:
                console.print(Text('Choose a longer password (at least 8 characters)', style='red'))
                password = ''
            else:
                encryptedPassword = EncryptPassword(password, key)
                StorePasswordData(website, username, encryptedPassword)
                console.print(Text('\nPassword saved successfully...\n', style='yellow'))
                return
        console.print(Text('\nFailed to save the password after multiple attempts.\n', style='red'))
    except Exception as e:
        console.print(Text(f'Error saving password: {e}', style='red'))


def RewritePasswords(oldKey, newKey):
    try:
        lines = ReadPasswords()
        updatedLines = []
        for line in lines:
            website, username, encryptedPassword = line.strip().split('\t')
            decryptedPassword = DecryptPassword(encryptedPassword, oldKey)
            newEncryptedPassword = EncryptPassword(decryptedPassword, newKey)
            updatedLines.append(f"{website}\t{username}\t{newEncryptedPassword.decode()}\n")
        WritePasswords(updatedLines)
        console.print(Text('Passwords updated successfully with the new Master Key.', style='green'))
    except Exception as e:
        console.print(Text(f'Error updating passwords: {e}', style='red'))
