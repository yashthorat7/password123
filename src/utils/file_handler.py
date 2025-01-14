import json
from ..utils.utils import color_print, clear_lines, color_input
from ..encryption.encrypter import encrypt

def read_json(file_name):
    '''Reads and returns JSON data from specified file.'''
    with open('./data/'+ file_name, 'r') as file:
        return json.load(file)

def write_json(file_name, data):
    '''Writes data to specified JSON file with proper formatting.'''
    with open('./data/'+ file_name, 'w') as file:
        json.dump(data, file, indent=4)

def get_master_key():
    '''Retrieves master key from settings file.'''
    return read_json('settings.json')['masterKey']

def ask_key():
    '''Prompts for master key with retry attempts.'''
    master_key = get_master_key()
    attempts = 5
    
    while attempts > 0:
        key = color_input('Enter the Master Key: ', 'cyan')
        clear_lines(1 if attempts == 5 else 2)
        
        if not key:
            color_print('Master Key cannot be empty!\n', 'red')
        elif key != master_key:
            color_print('Invalid Master Key!\n', 'red')
        else:
            return key            
        attempts -= 1

def save_password(website, username, password):
    '''Encrypts and saves password entry to storage file.'''
    encrypted_bytes = encrypt(password, get_master_key())
    encrypted_str = encrypted_bytes.decode('utf-8')
    
    new_entry = {'website': website, 'username': username, 'password': encrypted_str}
    
    try:
        with open('./data/passwords.json', 'r') as file:
            passwords = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = []
    
    passwords.append(new_entry)
    with open('./data/passwords.json', 'w') as file:
        json.dump(passwords, file, indent=4, ensure_ascii=False)

    
