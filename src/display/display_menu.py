from ..utils.utils import clear_lines, menu_list, color_print
from .handle_search import handle_search
from .handle_add import handle_add
from .handle_remove import handle_remove

MENU_CHOICES = [
    'Search a Password',
    'Add a Password',
    'Remove a Password',
    'Back'
]

def display_menu(table_clone):
    color_print('\n')
    choice = menu_list('Display Menu', MENU_CHOICES)
    clear_lines(6)

    if choice == 'Search a Password':
        handle_search(table_clone)
    elif choice == 'Add a Password':
        handle_add()
    elif choice == 'Remove a Password':
        handle_remove(table_clone)
    return choice != 'Back'