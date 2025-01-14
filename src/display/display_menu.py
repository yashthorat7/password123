from ..utils.utils import menu_list
from .handle_add import handle_add
from .handle_search import handle_search
from .handle_remove import handle_remove

def display_menu(table_data):
    '''Manages password display operations menu and navigation.'''
    menu_choices = [
        'Add a Password',
        'Search Passwords',
        'Remove a Password',
        'Back'
    ]
    
    choice = menu_list('Password Operations', menu_choices)
    
    if choice == 'Add a Password':
        handle_add()
    elif choice == 'Search Passwords':
        handle_search(table_data)
    elif choice == 'Remove a Password':
        handle_remove(table_data)
    else:
        return False
    return True