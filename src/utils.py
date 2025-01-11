import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.box import ROUNDED
from inquirer import confirm, List, prompt
from rich.table import Table

console = Console()

def clear_lines(lines=2):
    print('\033[A\033[K' * lines, end='')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def color_print(message, color='white'):
    console.print(Text(message, style=color), end='')

def confirm_print(message, set_to=True):
    return confirm(message, default=set_to)

def panel_print(password):
    password_text = Text('Generated Password: ', style='yellow2') + Text(password, style='green')
    console.print(Panel(password_text, style='bold', expand=False, box=ROUNDED))
    console.print('')

def menu_list(message_text, choice_list):
    menu_prompt = [List('menuChoice', message=message_text, choices=choice_list)]
    return prompt(menu_prompt).get('menuChoice')

def create_table(headers, rows, styles):
    table = Table(header_style='bold', box=ROUNDED)
    for header, style in zip(headers, styles):
        table.add_column(header, justify='left', style=style)
    for row in rows:
        table.add_row(*row)
    return table

def print_table(table):
    console.print(table)
    console.print('')

def paginate_data(headers, rows, styles, page_size=10):
    if len(rows) <= page_size:
        table = create_table(headers, rows, styles)
        print_table(table)
        return

    current_page = 0
    total_pages = (len(rows) + page_size - 1) // page_size

    while True:
        start_index = current_page * page_size
        end_index = start_index + page_size
        table = create_table(headers, rows[start_index:end_index], styles)

        print_table(table)
        color_print(f'\t\t\tPage {current_page + 1} of {total_pages}', 'cyan', '\n')

        choices = []
        if current_page > 0:
            choices.append("Previous")
        if current_page < total_pages - 1:
            choices.append("Next")
        choices.append("Menu")

        action = menu_list('Navigate pages', choices)

        if action == "Next": 
            clear_console()
            current_page += 1
        elif action == "Previous":
            clear_console()
            current_page -= 1
        elif action == "Menu":
            menu_size = len(choices) + 3
            print('\033[A\033[K' * menu_size, end='')
            break