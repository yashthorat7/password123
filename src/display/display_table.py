from ..utils import color_print, clear_console, create_table, print_table
import inquirer

def paginate_table(headers, rows, styles):
    page_size = 10
    current_page = 0
    total_pages = (len(rows) + page_size - 1) // page_size

    while True:
        start_index = current_page * page_size
        end_index = start_index + page_size
        table = create_table(headers, rows[start_index:end_index], styles)

        print_table(table)
        color_print(f'\t\t\tPage {current_page + 1} of {total_pages}', 'cyan', '\n')

        if total_pages == 1:
            return

        choices = []
        if current_page > 0:
            choices.append("Previous")
        if current_page < total_pages - 1:
            choices.append("Next")
        choices.append("Menu")

        action = inquirer.prompt([
            inquirer.List('action', message='Navigate pages', choices=choices)
        ])['action']

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