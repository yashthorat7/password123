from ..utils.utils import color_print, color_input
from ..utils.file_handler import read_json, write_json

def fix_password_length(to_fix):
    '''Configures fixed password length setting in application settings.'''
    if to_fix:
        while True:
            length = color_input('Enter a fixed length: ', 'cyan')
            try:
                length = int(length)
                if length < 8:
                    color_print('Password must be at least 8 characters long\n', 'red')
                elif length > 64:
                    color_print('Password must be at most 64 characters long\n', 'red')
                else:
                    data = read_json('settings.json')
                    data['default'] = length
                    data['defaultForce'] = True
                    # Clean up old key if present
                    if 'defaultForceNum' in data:
                        del data['defaultForceNum']
                    write_json('settings.json', data)
                    color_print(f'Password length set to {length} forever\n', 'green')
                    break
            except ValueError:
                color_print('Please enter a valid number\n', 'red')
    else:
        data = read_json('settings.json')
        data['defaultForce'] = False
        write_json('settings.json', data)
        color_print('Password length will be asked every time', 'green')
    color_input('\nPress enter to continue...', '#4a4a4a')