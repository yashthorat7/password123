from ..utils.utils import color_print, clear_lines
from ..utils.file_handler import read_json, write_json

def fix_password_length(to_fix):
    if to_fix:
        while True:
            color_print('Enter a fixed length: ', 'cyan')
            length = input()
            try:
                length = int(length)
                if length < 8:
                    color_print('Password must be at least 8 characters long\n', 'red')
                elif length > 64:
                    color_print('Password must be at most 64 characters long\n', 'red')
                else:
                    data = read_json('settings.json')
                    data['defaultForceNum'] = length
                    data['defaultForce'] = True
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
    input()