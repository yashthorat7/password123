from ..file_handle import read_json
from ..utils import color_print, clear_lines

def ask_length(default):
    color_print('Enter the length ', 'cyan')
    color_print(f'(default: {default})', 'blue')
    color_print(': ', 'cyan')
    user_input = input()
    return int(user_input) if user_input else default

def valid_length(length, first_time):
    try:
        length = int(length)
    except ValueError:
        clear_lines(1 if first_time else None)
        color_print('Length is invalid! It must be a number.\n', 'red')
        return False

    if 8 <= length <= 64:
        return True

    clear_lines(1 if first_time else None)
    color_print('Length should be at least 8\n', 'red') if length < 8 else color_print('Length should be at most 64\n', 'red')
    return False

def generate_length(state):
    settings_data = read_json('settings.json')
    has_default = settings_data['defaultForce']

    if not state or not has_default:
        first_time = True
        while True:
            length = ask_length(settings_data['default'])
            if valid_length(length, first_time):
                return return_sequence(length)
            first_time = False
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
