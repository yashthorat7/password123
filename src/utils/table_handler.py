from rich.table import Table
from rich.console import Console
from rich.box import ROUNDED
from ..utils.utils import color_print, menu_list, clear_lines
from ..display_title import display_title

console = Console()

def create_table(headers, rows, styles):
    '''Creates rich table with specified headers and styling.'''
    table = Table(header_style='bold', box=ROUNDED)
    for header, style in zip(headers, styles):
        table.add_column(header, justify='left', style=style)
    for row in rows:
        table.add_row(*row)
    return table

def print_table(table):
    '''Prints rich table to console.'''
    console.print(table)

def paginate_table(headers, rows, styles):
    '''Displays table data with pagination controls.'''
    page_size = 10
    
    if len(rows) <= page_size:
        table = create_table(headers, rows, styles)
        print_table(table)
        return
        
    current_page = 0
    total_pages = (len(rows) + page_size - 1) // page_size

    while True:
        start_index = current_page * page_size
        end_index = min(start_index + page_size, len(rows))
        current_rows = rows[start_index:end_index]
        
        table = create_table(headers, current_rows, styles)
        print_table(table)

        color_print(f'\t\t\tPage {current_page + 1} of {total_pages}\n', 'cyan')

        choices = []
        if current_page < total_pages - 1:
            choices.append('Next')
        if current_page > 0:
            choices.append('Previous')
        choices.append('Menu')

        action = menu_list('Navigate pages', choices)

        if action == 'Previous':
            display_title()
            current_page -= 1
        elif action == 'Next':
            display_title()
            current_page += 1
        elif action == 'Menu':
            clear_lines(len(choices) + 3)
            return True