from ..utils.utils import color_print, confirm_print
from ..utils.file_handler import read_json, write_json

def handle_remove(table_data):
    """Removes password entries based on serial number."""
    if not table_data:
        color_print('No passwords to remove!\n', 'red')
        input()
        return
        
    color_print('Enter Sr.no. to remove: ', 'cyan')
    try:
        index = int(input()) - 1
        if 0 <= index < len(table_data):
            website = table_data[index][1]
            if confirm_print(f'Remove password for {website}?', False):
                passwords = read_json('passwords.json')
                passwords.pop(index)
                write_json('passwords.json', passwords)
                color_print('Password removed successfully!\n', 'green')
        else:
            color_print('Invalid serial number!\n', 'red')
    except ValueError:
        color_print('Please enter a valid number!\n', 'red')
    input()