from ..utils.utils import menu_list, color_print, confirm_print
from ..utils.file_handler import read_json, write_json, save_password, get_master_key
from ..encryption.encrypter import encrypt
from ..encryption.decrypter import decrypt
import json
import os

def process_password_entry(entry, is_encrypted, key):
    decrypted_pass = decrypt(entry['password'], get_master_key())
    if decrypted_pass == '[Error]':
        return None
    return encrypt(decrypted_pass, key) if is_encrypted else decrypted_pass

def handle_file_operation(operation, location, retry_prompt='Would you like to try a different location?'):
    try:
        return operation()
    except (FileNotFoundError, PermissionError, OSError) as e:
        error_msg = 'File not found!' if isinstance(e, FileNotFoundError) else 'Permission denied!' if isinstance(e, PermissionError) else f'Invalid file location: {str(e)}'
        color_print(f'Error: {error_msg}', 'red')
        return None if not confirm_print(retry_prompt, True) else 'retry'
    except Exception as e:
        color_print(f'Unexpected error: {str(e)}', 'red')
        return None

def import_file():
    is_encrypted = confirm_print('Is your file encrypted?', False)

    while True:
        color_print('Enter file location (including filename.json): ', 'cyan')
        location = input()
        if not location.endswith('.json'):
            location += '.json'

        def read_operation():
            with open(location, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError('Invalid file format! Expected a list of password entries.')
                return data

        imported_data = handle_file_operation(read_operation, location)
        if imported_data is None:
            return
        if imported_data == 'retry':
            continue

        if is_encrypted:
            color_print('Enter decryption key: ', 'cyan')
            decrypt_key = input()
            if not decrypt_key:
                color_print('Decryption key cannot be empty!', 'red')
                return

            for entry in imported_data:
                if 'password' in entry:
                    decrypted_pass = decrypt(entry['password'], decrypt_key)
                    if decrypted_pass == '[Error]':
                        color_print('Failed to decrypt passwords. Invalid key or corrupted data.', 'red')
                        return
                    save_password(entry['website'], entry['username'], decrypted_pass)
        else:
            for entry in imported_data:
                if all(k in entry for k in ('website', 'username', 'password')):
                    save_password(entry['website'], entry['username'], entry['password'])

        color_print('Files imported successfully!', 'green')
        break

def export_file():
    need_encryption = confirm_print('Export an encrypted file?', False)

    try:
        passwords = read_json('passwords.json')
        if not passwords:
            color_print('No passwords to export!', 'red')
            return
        
        key = None
        if need_encryption:
            color_print('Enter encryption key: ', 'cyan')
            key = input()
            if not key:
                color_print('Encryption key cannot be empty!', 'red')
                return

        export_data = []
        for entry in passwords:
            new_entry = entry.copy()
            processed_pass = process_password_entry(entry, need_encryption, key)
            if processed_pass is None:
                color_print('Failed to process passwords. Please try again.', 'red')
                return
            new_entry['password'] = processed_pass
            export_data.append(new_entry)

        while True:
            color_print('Enter export file location (folder path): ', 'cyan')
            export_location = input()
            
            color_print('Enter file name (without .json): ', 'cyan')
            file_name = input() or 'passwords'
            full_path = os.path.join(export_location, file_name + '.json')

            def write_operation():
                if export_location:
                    os.makedirs(export_location, exist_ok=True)
                with open(full_path, 'w', encoding='utf-8') as file:
                    json.dump(export_data, file, indent=4, ensure_ascii=False)
                return os.path.exists(full_path)

            result = handle_file_operation(write_operation, full_path)
            if result is None:
                return
            if result == 'retry':
                continue
            if result:
                color_print(f'Files exported successfully to: {full_path}', 'green')
                break
            else:
                color_print('Failed to create export file!', 'red')

    except Exception as e:
        color_print(f'Error exporting file: {str(e)}', 'red')

def import_export():
    menu_choices = [
        'Import a file',
        'Export a file'
    ]
    
    choice = menu_list('Import/Export files', menu_choices)
    if choice == 'Import a file':
        import_file()
    elif choice == 'Export a file':
        export_file()
    input()
    

