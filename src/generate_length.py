from .file_handle import read_json
from .utils import color_print

def generate_length(state):
    settings_data = read_json('settings.json')
    has_default = settings_data['defaultForce']

    if not state or not has_default:
        default = settings_data['default']
        color_print('Enter the length ', 'cyan')
        color_print(f'(default: {default})', 'blue')
        color_print(': ', 'cyan')
        length = int(input())
        
        return return_sequence(length)
    
    return return_sequence(int(settings_data['defaultForceNum']))

def get_structure(length):
    digits = max(1, length // 8)
    capital_letters = max(1, length // 16)
    symbols = max(2, length // 8)
    small_letters = length - (digits + capital_letters + symbols)
    return [digits, capital_letters, symbols, small_letters]

def return_sequence(length):
    structure = get_structure(length)
    return length, structure