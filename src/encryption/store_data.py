from ..utils.utils import clear_lines, color_print
from ..utils.file_handler import save_password, read_json, write_json
from .encrypter import encrypt
from .decrypter import decrypt

def ask_username():
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
    color_print('Enter the Password: ', 'cyan')
    password = input()
    return password

def rewrite_passwords(old_key, new_key):
    try:
        lines = read_json('passwords.json')
        updated_lines = []
        for line in lines:
            website, username, encrypted_password = line.strip().split('\t')
            decrypted_password = decrypt(encrypted_password, old_key)
            new_encrypted_password = encrypt(decrypted_password, new_key)
            updated_lines.append(f'{website}\n{username}\n{new_encrypted_password.decode()}\n')
        write_json(updated_lines)
        return True
    except Exception as e:
        raise Exception(f'Error updating passwords: {e}')       

def store_data(password):
    clear_lines(5)
    website, username = ask_username();
    if isinstance(password, bytes):
        password = ask_password()
        password = password.decode('utf-8')
    
    save_password(website, username, password)
    color_print('\nPassword saved sucessfully...', 'green')
    input()
