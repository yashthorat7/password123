from ..utils.utils import color_print
from ..utils.file_handler import ask_key, read_json, write_json
from .data_handler import rewrite_passwords

def change_master_key():
    key = ask_key()
    if not key:
        return

    color_print('Enter the new Master Key: ', 'cyan')
    new_key = input()
    if not new_key:
        color_print('\nMaster Key cannot be empty!\n', 'red')
        return

    try:
        rewrite_passwords(key, new_key)
        
        settings = read_json('settings.json')
        settings['masterKey'] = new_key
        write_json('settings.json', settings)

        color_print('Master Key changed successfully!\n', 'green')
        input()
    except Exception as e:
        color_print(f'Error changing master key: {str(e)}\n', 'red')
        input()