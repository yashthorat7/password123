from ..utils.utils import menu_list, color_print, confirm_print, color_input
from ..utils.file_handler import read_json, write_json, save_password, get_master_key
from ..display.display import display_title
from ..encryption.encrypter import encrypt
from ..encryption.decrypter import decrypt
import json
import os

def process_password_entry(entry, is_encrypted, key):
    '''Processes password entry for import/export with encryption handling.'''
    if not is_encrypted:
        decrypted_pass = decrypt(entry['password'], get_master_key())
        return decrypted_pass if decrypted_pass != '[Error]' else None
    else:
        decrypted_pass = decrypt(entry['password'], get_master_key())
        if decrypted_pass == '[Error]':
            return None
        encrypted_bytes = encrypt(decrypted_pass, key)
        return encrypted_bytes.decode('utf-8')

def import_file():
    '''Imports passwords from JSON file with encryption support.'''
    is_encrypted = confirm_print('Is your file encrypted?', False)
    
    location = color_input('Enter file location (including filename.json): ', 'cyan')
    if not location.endswith('.json'):
        location += '.json'

    try:
        with open(location, 'r', encoding='utf-8') as file:
            imported_data = json.load(file)
            if not isinstance(imported_data, list):
                color_print('Invalid file format! Expected a list of password entries.', 'red')
                return

        if is_encrypted:
            decrypt_key = color_input('Enter decryption key: ', 'cyan')
            if not decrypt_key:
                color_print('Decryption key cannot be empty!', 'red')
                return

        for entry in imported_data:
            if all(k in entry for k in ('website', 'username', 'password')):
                if is_encrypted:
                    decrypted_pass = decrypt(entry['password'], decrypt_key)
                    if decrypted_pass == '[Error]':
                        color_print('Failed to decrypt passwords. Invalid key or corrupted data.', 'red')
                        return
                    save_password(entry['website'], entry['username'], decrypted_pass)
                else:
                    save_password(entry['website'], entry['username'], entry['password'])

        color_print('Files imported successfully!', 'green')

    except FileNotFoundError:
        color_print('File not found!', 'red')
    except Exception as e:
        color_print(f'Error importing file: {str(e)}', 'red')

def export_file():
    '''Exports passwords to JSON file with encryption option.'''
    need_encryption = confirm_print('Export an encrypted file?', False)

    try:
        passwords = read_json('passwords.json')
        if not passwords:
            color_print('No passwords to export!', 'red')
            return
        
        key = None
        if need_encryption:
            key = color_input('Enter encryption key: ', 'cyan')
            if not key:
                color_print('Encryption key cannot be empty!', 'red')
                return

        export_data = []
        for entry in passwords:
            processed_pass = process_password_entry(entry, need_encryption, key)
            if processed_pass is None:
                color_print('Failed to process passwords. Please try again.', 'red')
                return
            export_data.append({
                'website': entry['website'],
                'username': entry['username'],
                'password': processed_pass
            })

        export_location = color_input('Enter export file location (folder path): ', 'cyan')
        
        file_name = color_input('Enter file name (without .json): ', 'cyan') or 'passwords'
        full_path = os.path.join(export_location, file_name + '.json')

        if export_location:
            os.makedirs(export_location, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as file:
            json.dump(export_data, file, indent=4, ensure_ascii=False)
        
        color_print(f'Files exported successfully to: {full_path}', 'green')

    except Exception as e:
        color_print(f'Error exporting file: {str(e)}', 'red')

def import_export():
    '''Manages import and export functionality through menu options.'''
    menu_choices = [
        'Import a file',
        'Export a file',
        'Back'
    ]
    
    choice = menu_list('Import/Export files', menu_choices)
    display_title()
    if choice == 'Import a file':
        import_file()
    elif choice == 'Export a file':
        export_file()
    else:
        return
    color_input('\nPress enter to continue...', '#4a4a4a')
    