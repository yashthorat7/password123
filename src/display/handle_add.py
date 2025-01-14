from ..encryption.store_data import store_data
from ..utils.utils import color_print, color_input

def handle_add():
    '''Handles adding new password entries to storage.'''
    try:
        store_data()
    except Exception as e:
        color_print(f'Error adding password: {e}\n', 'red')