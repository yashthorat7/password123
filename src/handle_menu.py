from .display_title import display_title
from .utils import clear_lines
from inquirer import confirm
from rich.text import Text
from rich.console import Console

console = Console()

def handle_menu(choice):
    display_title()
    if choice == 'Generate a Password':
        pass
    elif choice == 'Display the Passwords':
        pass
    elif choice == 'Settings':
        pass
    elif choice == 'Exit':
        if confirm('Exit the program?', default=True):
            clear_lines(2)
            console.print(Text('Exited...', style='red'))
            console.print(Text('--coded by Yash Thorat', style='red'))
            exit(0)