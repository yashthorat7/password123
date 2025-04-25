from src.main_menu import main_menu
from src.utils.file_handler import get_master_key
from src.startup import startup

def main():
    '''Entry point for Password123 application.'''
    if get_master_key() == '':
        startup()
    while True:
        main_menu()

if __name__ == '__main__':
    main()