import json
from .utils import clear_lines, color_print

def read_json(file_name):
    with open('./data/'+ file_name, 'r') as file:
        return json.load(file)

def ask_key():
    master_key = read_json('settings.json')['masterKey']
    attempts = 5
    
    while attempts > 0:
        color_print('Enter the Master Key: ', 'cyan')
        key = input()
        clear_lines(1 if attempts == 5 else 2)
        
        if not key:
            color_print('Master Key cannot be empty!\n', 'red')
        elif key != master_key:
            color_print('Invalid Master Key!\n', 'red')
        else:
            return key            
        attempts -= 1