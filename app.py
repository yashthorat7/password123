from src.display_title import display_title
from src.handle_menu import handle_menu
from src.utils import menu_list

MENU_CHOICES = [
    'Generate a Password',
    'Display the Passwords',
    'Settings',
    'Exit',
]

def render_menu():
    choice = menu_list('Main Menu', MENU_CHOICES)
    handle_menu(choice)

def main():
    while True:
        display_title()
        render_menu()

if __name__ == '__main__':
    main()