from ..utils.utils import color_print, confirm_print
from ..utils.file_handler import read_json, write_json, ask_key
from ..encryption.encrypter import encrypt
from ..encryption.decrypter import decrypt

def rewrite_passwords(key, new_key):
    """Re-encrypts all stored passwords with new master key."""
    try:
        passwords = read_json('passwords.json')
        if not passwords:
            return
            
        new_passwords = []
        for entry in passwords:
            try:
                decrypted_password = decrypt(entry['password'], key)
                new_entry = {
                    'website': entry['website'],
                    'username': entry['username'],
                    'password': encrypt(decrypted_password, new_key)
                }
                new_passwords.append(new_entry)
            except Exception as e:
                raise Exception(f"Failed to process entry for {entry.get('website', 'unknown')}: {str(e)}")
                
        write_json('passwords.json', new_passwords)
    except FileNotFoundError:
        write_json('passwords.json', [])
    except Exception as e:
        raise Exception(f"Failed to rewrite passwords: {str(e)}")

def erase_data():
    """Securely erases all stored password data after confirmation."""
    key = ask_key()
    if not key:
        return

    if confirm_print('Are you sure you want to erase all the data?', False):
        write_json('passwords.json', [])
        color_print('Data Erased Successfully!\n', 'green')
        input()