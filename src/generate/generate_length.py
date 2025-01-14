from ..utils.file_handler import read_json
from ..display_title import display_title
from ..utils.utils import color_print, clear_lines, color_input

def ask_length(default):
    '''Prompts for password length with default value option.'''
    color_print('Enter the length ', 'cyan')
    color_print(f'(default: {default})', 'blue')
    user_input = color_input(': ', 'cyan')
    if not user_input:
        return default
    try:
        return int(user_input)
    except ValueError:
        return 'invalid'

def valid_length(length, first_time):
    '''Validates if password length meets required criteria.'''
    if first_time:
        clear_lines(1)
    else:
        clear_lines()

    if length == 'invalid':
        color_print('Length is invalid! It must be a number.\n', 'red')
        return False

    if 8 <= length <= 64:
        return True

    if length < 8:
        color_print('Length should be at least 8\n', 'red')
    else:
        color_print('Length should be at most 64\n', 'red')
        
    return False

def generate_length(state):
    '''Determines password length based on user input or settings.'''
    settings_data = read_json('settings.json')
    has_default = settings_data['defaultForce']

    if not state or not has_default:
        first_time = True
        for _ in range(5):
            length = ask_length(settings_data['default'])
            if valid_length(length, first_time):
                return return_sequence(length)
            first_time = False
    return return_sequence(int(settings_data['defaultForceNum']))

def get_structure(length):
    '''Calculates character type distribution for password length.'''
    digits = max(1, length // 8)
    capital_letters = max(1, length // 16)
    symbols = max(2, length // 8)
    small_letters = length - (digits + capital_letters + symbols)
    return [digits, capital_letters, symbols, small_letters]

def return_sequence(length):
    '''Returns password length with its character structure.'''
    structure = get_structure(length)
    return length, structure
