from ..display_title import display_title
from .display_data import display_data, tableClone
from .display_menu import display_menu
from ..utils import clear_console, color_print
import json

SETTINGS_FILE = 'data/settings.json'

def get_master_key():
    try:
        with open(SETTINGS_FILE, 'r') as file:
            settings = json.load(file)
            return settings['masterKey']
    except Exception as e:
        color_print(f'Error loading master key: {e}\n', 'red')
        return None

def display():
    try:
        master_key = get_master_key()
        if not master_key:
            return
            
        clear_console()
        while True:
            display_title()
            if not display_data(master_key):
                break
                
            if not display_menu(tableClone, master_key):
                clear_console()
                break
                
            clear_console()
            
    except Exception as e:
        color_print(f'Unexpected error: {e}\n', 'red')
