from .display_title import display_title
from .utils import clear_lines, color_print, confirm_print, menu_list
from .generate.generate import generate
from .display.display import display

MENU_CHOICES = [
    'Generate a Password',
    'Display the Passwords',
    'Settings',
    'Exit',
]

def handle_menu(choice):
    if choice == 'Generate a Password':
        generate()
    elif choice == 'Display the Passwords':
        display()
    elif choice == 'Settings':
        pass
    elif choice == 'Exit':
        display_title()
        has_confirmed = confirm_print('Exit the Program?')
        if has_confirmed:
            clear_lines()
            color_print('Exited------------------------------------------------Yash Thorat', 'red')
            exit(0)

def main_menu():
    display_title()
    choice = menu_list('Main Menu', MENU_CHOICES)
    handle_menu(choice)