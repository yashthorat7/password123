from ..utils.file_handler import read_json, write_json
from ..display_title import display_title
from .settings_menu import settings_menu

def set_json_attribute(attribute, value):
    data = read_json('settings.json')
    data[attribute] = value
    write_json('settings.json', data)

def settings():
    while True:
        display_title()
        if not settings_menu():
            break
