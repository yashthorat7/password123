from .utils.utils import color_print, color_input, clear_console, clear_lines
from .utils.file_handler import write_json, read_json
from .encryption.encrypter import encrypt

def startup():
    '''Initializes a master key'''
    clear_console()
    color_print('[New User]\n', 'yellow')

    while True:
        master_key = color_input('Set a Master Key: ', 'cyan')
        if not master_key:
            clear_console()
            color_print('Master Key cannot be empty!\n', 'red')
            continue
        confirm_key = color_input('Confirm Master Key: ', 'cyan')
        if master_key != confirm_key:
            clear_console()
            color_print('Keys do not match. Please try again.\n', 'red')
        else:
            break

    settings = read_json('settings.json')
    encrypted_key = encrypt(master_key, 'default_key')
    settings['masterKey'] = encrypted_key.decode('utf-8')
    write_json('settings.json', settings)
    color_print('Master Key saved successfully!\n', 'green')
    color_input('Press enter to continue...', '#4a4a4a')
