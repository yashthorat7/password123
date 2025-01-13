from ..utils.utils import clear_lines, menu_list
from ..encryption.store_data import store_data

MENU_CHOICES = [
    'Yes',
    'No',
    'Generate Again',
]

def handle_menu(choice, password):
    if choice == 'Yes':
        clear_lines(5)
        store_data(password)
    elif choice == 'No':
        pass
    elif choice == 'Generate Again':
        return False
    return True

def generate_menu(password):
    choice = menu_list('Save the Password?', MENU_CHOICES)
    return handle_menu(choice, password)