from ..utils.utils import menu_list, clear_lines
from ..utils.file_handler import read_json
from .password_settings import fix_password_length
from .import_export import import_export
from .master_key import change_master_key
from .data_handler import erase_data
from ..display_title import display_title

def settings_menu():
    settings_data = read_json('settings.json')
    
    default_force = settings_data.get('defaultForce', False)
    password_status = 'Fix Password Length' if not default_force else 'Unfix Password Length'

    menu_choices = [
        password_status,
        'Import/Export files',
        'Change the Master Key',
        'Erase All Data',
        'Back'
    ]

    user_choice = menu_list('Settings', menu_choices)
        
    display_title()
    if user_choice == 'Fix Password Length':
        fix_password_length(True)
    elif user_choice == 'Unfix Password Length':
        fix_password_length(False)
    elif user_choice == 'Import/Export files':
        import_export()
    elif user_choice == 'Change the Master Key':
        change_master_key()
    elif user_choice == 'Erase All Data':
        erase_data()
    else:
        return False
    return True 