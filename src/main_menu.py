from .display_title import display_title
from .utils.utils import color_print, confirm_print, menu_list, clear_lines
from .generate.generate import generate
from .display.display import display
from .settings.settings import settings

MENU_CHOICES = [
    'Generate a Password',
    'Display the Passwords',
    'Settings',
    'Exit',
]

def exit_program():
    '''Handles program exit with user confirmation.'''
    display_title()
    has_confirmed = confirm_print('Exit the Program?')
    clear_lines()
    if has_confirmed:
        color_print('Exited------------------------------------------------Yash Thorat\n', 'red')
        exit(0)

def handle_menu(choice):
    '''Routes menu choices to appropriate function handlers.'''
    if choice == 'Generate a Password':
        generate()
    elif choice == 'Display the Passwords':
        display()
    elif choice == 'Settings':
        settings()
    elif choice == 'Exit':
        exit_program()

def main_menu():
    '''Displays main menu and handles user navigation.'''
    display_title()
    choice = menu_list('Main Menu', MENU_CHOICES)
    handle_menu(choice)