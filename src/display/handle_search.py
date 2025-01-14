from ..display_title import display_title
from ..utils.utils import color_print, color_input
from ..utils.table_handler import paginate_table

def handle_search(table_clone):
    '''Searches and displays passwords matching website name query.'''
    website = color_input('Enter the Website: ', 'cyan').strip()
    
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
    color_input('\nPress enter to continue...', '#4a4a4a')