from ..display_title import display_title
from ..utils.utils import clear_lines, color_print, clear_console
from ..utils.table_handler import paginate_table

def handle_search(table_clone):
    """Searches and displays passwords matching website name query."""
    color_print('Enter the Website: ', 'cyan')
    website = input().strip()
    
    if not website:
        color_print('Search term cannot be empty\n', 'red')
        return
        
    matched_rows = [row for row in table_clone if website.lower() in row[1].lower()]
    display_title()

    if matched_rows:
        headers = ['Sr.no.', 'Website', 'Username', 'Password']
        styles = ['red', 'orange3', 'yellow', 'green']
        paginate_table(headers, matched_rows, styles)
    else:
        color_print('No matches found\n', 'red')
    input()