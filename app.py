import inquirer
from rich.console import Console
from rich.text import Text
from src.display_title import display_title

console = Console()

MENU_CHOICES = [
    'Generate a Password',
    'Display the Passwords',
    'Settings',
    'Exit',
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
        confirm_exit = inquirer.confirm('Exit the program?', default=True)
        if confirm_exit:
            print('\033[A\033[K' * 2, end='')
            console.print(Text('Exited...', style='red'))
            console.print(Text('made by Yash Thorat', style='red'))
            exit(0)

def MainMenu():
    '''renders the main menu using inquirer''' 
    menuPrompt = [inquirer.List('menuChoice', message='What would you like to do?', choices=MENU_CHOICES)]
    choice = inquirer.prompt(menuPrompt)
    choice = choice['menuChoice']
    handleMenuChoice(choice)

def main():
    '''main function'''
    while True:
        display_title()
        MainMenu()

# run
if __name__ == '__main__':
    main()
