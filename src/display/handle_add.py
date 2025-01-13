from ..encryption.store_data import store_data
from ..utils.utils import color_print

def handle_add():
    try:
        store_data()
    except Exception as e:
        color_print(f'Error adding password: {e}\n', 'red')
    input()