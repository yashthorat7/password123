from ..utils import color_print, clear_console, create_table, print_table, menu_list, clear_lines
from ..display_title import display_title

def paginate_table(headers, rows, styles):
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
        # clear_lines(1)
        color_print(f'\t\t\tPage {current_page + 1} of {total_pages}\n', 'cyan')

        choices = []
        if current_page < total_pages - 1:
            choices.append("Next")
        if current_page > 0:
            choices.append("Previous")
        choices.append("Menu")

        action = menu_list('Navigate pages', choices)

        if action == "Previous":
            display_title()
            current_page -= 1
        elif action == "Next":
            display_title()
            current_page += 1
        elif action == "Menu":
            clear_lines(len(choices) + 3)
            break 