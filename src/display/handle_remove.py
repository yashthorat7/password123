from ..display_title import display_title
from ..utils.utils import clear_lines, color_print, confirm_print
from ..utils.file_handler import read_json, write_json
from ..utils.table_handler import paginate_table

def handle_remove(table_clone):
    try:
        color_print('Enter the serial No: ', 'cyan')
        row_index = int(input()) - 1
        if 0 <= row_index < len(table_clone):
            headers = ['Sr.no.', 'Website', 'Username', 'Password']
            styles = ['red', 'orange3', 'yellow', 'green']

            display_title()
            paginate_table(headers, [table_clone[row_index]], styles)

            if confirm_print('Remove this password?'):
                passwords = read_json('passwords.json')
                del passwords[row_index]
                write_json('passwords.json', passwords)
                color_print('Password removed successfully\n', 'yellow')
                input()
            else:
                color_print('Operation cancelled\n', 'cyan')
        else:
            color_print('Invalid serial number\n', 'red')
    except ValueError:
        color_print('Please enter a valid number\n', 'red')
    except Exception as e:
        color_print(f'Error removing password: {e}\n', 'red')