import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.box import ROUNDED
from inquirer import confirm, List, prompt

console = Console()

def clear_lines(lines=2):
    """Clears specified number of lines from console output."""
    print('\033[A\033[K' * lines, end='')

def clear_console():
    """Clears entire console screen based on OS type."""
    os.system('cls' if os.name == 'nt' else 'clear')

def color_print(message, color='white'):
    """Prints colored text to console using rich formatting."""
    console.print(Text(message, style=color), end='')

def confirm_print(message, set_to=True):
    """Displays confirmation prompt with customizable default value."""
    return confirm(message, default=set_to)

def panel_print(password):
    """Displays password in a styled panel with border."""
    password_text = Text('Generated Password: ', style='yellow2') + Text(password, style='green')
    console.print(Panel(password_text, style='bold', expand=False, box=ROUNDED))
    console.print('')

def menu_list(message_text, choice_list):
    """Creates interactive menu with provided choices and message."""
    menu_prompt = [List('menuChoice', message=message_text, choices=choice_list)]
    return prompt(menu_prompt).get('menuChoice')