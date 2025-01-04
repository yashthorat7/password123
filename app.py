import os
import inquirer
from rich.console import Console
from rich.text import Text
from src.display_title import run

console = Console()

MENU_CHOICES = [
    'Generate a Password',
    'Display the Passwords',
    'Settings',
    'Exit'
]


def handleMenuChoice(userChoice):
    '''calls function according to the user's choice'''
    if userChoice == 'Generate a Password':
        # generator()
        pass
    elif userChoice == 'Display the Passwords':
        # display()
        pass
    elif userChoice == 'Settings':
        # settings()
        pass
    elif userChoice == 'Exit':
        confirm_exit = inquirer.confirm('Are you sure you want to exit?', default=True)
        if confirm_exit:
            print('\033[A\033[K' * 1, end='')
            console.print(Text('Exiting the tool...', style='red'))
            exit(0)


def MainMenu():
    '''renders the main menu using inquirer''' 
    try:
        menuPrompt = [inquirer.List('menuChoice', message='What would you like to do?', choices=MENU_CHOICES)]
        choice = inquirer.prompt(menuPrompt)
        if not choice or 'menuChoice' not in choice:
            console.print(Text('Invalid selection. Please try again.', style='red'))
            return
        handleMenuChoice(choice['menuChoice'])
    except Exception as e:
        console.print(f'Error: {e}', style='red')


def main():
    '''main function'''
    while True:
        try:
            run()
            MainMenu()
        except KeyboardInterrupt:
            console.print(Text('Exiting the tool...', style='red2'))
            break


# run
if __name__ == '__main__':
    main()
