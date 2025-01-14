from ..utils.utils import clear_lines, color_print
from ..utils.file_handler import save_password, read_json, write_json
from .encrypter import encrypt
from .decrypter import decrypt

def ask_username():
    """Prompts for website and username with default handling."""
    color_print('Enter the Website: ', 'cyan')
    website = input()
    color_print('Enter the Username: ', 'cyan')
    username = input()

    if website == '':
        website = 'N/A'
    if username == '':
        username = 'N/A'

    return website, username

def ask_password():
    """Prompts user to enter password for storage."""
    color_print('Enter the Password: ', 'cyan')
    password = input()
    return password      

def store_data(password = ''):
    """Stores password entry with website and username details."""
    website, username = ask_username()
    if password == '':
        password = ask_password()

    if isinstance(password, bytes):
        password = password.decode('utf-8')
    
    if password != '':
        save_password(website, username, password)
        color_print('\nPassword saved successfully...', 'green')
    else:
        color_print('\nFailed saving the password', 'red')
        
    input()
