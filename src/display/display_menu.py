from ..utils.utils import menu_list, color_print, clear_console, confirm_print, clear_lines
from ..utils.file_handler import read_json, write_json
from ..utils.table_handler import paginate_table
from ..display_title import display_title
from ..encryption.store_data import store_data
from ..encryption.encrypter import encrypt

MENU_CHOICES = [
    'Search a Password',
    'Add a Password',
    'Remove a Password',
    'Back'
]

def handle_search(table_clone):
    color_print('Enter the Website: ', 'cyan')
    website = input() or 'N/A'
    matched_rows = [row for row in table_clone if row[1].lower() == website.lower()]
    print('\033[A\033[K' * 1, end='')
    clear_console()
    
    if matched_rows:
        headers = ['Sr.no.', 'Website', 'Username', 'Password']
        styles = ['orange3', 'cyan', 'red', 'yellow']
        paginate_table(headers, matched_rows, styles)
        display_title()
    else:
        color_print('No match found\n', 'red')

def handle_add(master_key):
    try:
        store_data()
        print('\033[A\033[K' * 8, end='')
        clear_console()
    except Exception as e:
        color_print(f'Error adding password: {e}\n', 'red')

def handle_remove(table_clone):
    try:
        color_print('Enter the serial No: ', 'cyan')
        row_index = int(input()) - 1
        if 0 <= row_index < len(table_clone):
            headers = ['Sr.no.', 'Website', 'Username', 'Password']
            styles = ['yellow', 'red', 'magenta', 'red']
            paginate_table(headers, [table_clone[row_index]], styles)
            display_title()
            
            if confirm_print('Are you sure you want to remove this password?'):
                lines = read_json('passwords.json')
                del lines[row_index]
                write_json(lines)
                color_print('Password removed successfully\n', 'yellow')
            else:
                color_print('Operation cancelled\n', 'cyan')
        else:
            color_print('Invalid serial number\n', 'red')
        print('\033[A\033[K' * 11, end='')
        clear_console()
    except ValueError:
        color_print('Please enter a valid number\n', 'red')
    except Exception as e:
        color_print(f'Error removing password: {e}\n', 'red')

def display_menu(table_clone, master_key):
    color_print('\n')
    choice = menu_list('Display Menu', MENU_CHOICES)
    
    if choice == 'Search a Password':
        handle_search(table_clone)
    elif choice == 'Add a Password':
        handle_add(master_key)
    elif choice == 'Remove a Password':
        handle_remove(table_clone)
    
    return choice != 'Back' 