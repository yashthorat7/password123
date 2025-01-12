from .display_data import display_data, tableClone
from .display_menu import display_menu
from ..utils.file_handler import ask_key
from ..display_title import display_title

def display():
    master_key = ask_key()

    if not master_key:
        return
    while True:
        display_title()
        if not display_data(master_key):
            break
        if not display_menu(tableClone, master_key):
            display_title()
            break
