from ..utils import menu_list

MENU_CHOICES = [
    'Yes',
    'No',
    'Generate Again',
]

def handle_menu(choice):
    if choice == 'Yes':
        pass
    elif choice == 'No':
        pass
    elif choice == 'Generate Again':
        return False
    return True

def generate_menu():
    choice = menu_list('Save the Password?', MENU_CHOICES)
    return handle_menu(choice)