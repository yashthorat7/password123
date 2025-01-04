from rich.console import Console
from rich.text import Text
from inquirer import List, confirm, prompt

console = Console()

def clear_lines(lines):
    print('\033[A\033[K' * lines, end='')

def color_print(message, color = 'white'):
    console.print(Text(message, style=color))

def menu_list(message_text, choice_list):
    menu_prompt = [List('menuChoice', message=message_text, choices=choice_list)]
    return prompt(menu_prompt).get('menuChoice')