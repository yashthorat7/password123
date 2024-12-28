import os
import inquirer
from rich.console import Console
from rich.text import Text
from src.generator import generator
from src.display import display
from src.settings import settings

console = Console()

TITLE_TEXT = [
    ('bold #ff5ca8', r' ____   _    ____ ______        _____  ____  ____  _ ____  _____ '),
    ('bold #ff70a1', r'|  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \/ |___ \|___ / '),
    ('bold #ff8c8b', r'| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | | | __) | |_ \ '),
    ('bold #ffa168', r'|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| | |/ __/ ___) |'),
    ('bold #ffa724', r'|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/|_|_____|____/ '),
]

MENU_CHOICES = [
    'Generate a Password',
    'Display the Passwords',
    'Settings',
    'Exit'
]


def DisplayTitle():
    '''displays the title text'''
    os.system('cls' if os.name == 'nt' else 'clear')    #clears the console
    for color, line in TITLE_TEXT:
        styledTitle = Text(line, style=color)
        console.print(styledTitle)
    console.print('')


def handleMenuChoice(userChoice):
    '''calls function according to the user's choice'''
    try:
        if userChoice == 'Generate a Password':
            generator()
        elif userChoice == 'Display the Passwords':
            display()
        elif userChoice == 'Settings':
            settings()
        elif userChoice == 'Exit':
            confirm_exit = inquirer.confirm("Are you sure you want to exit?", default=True)
            if confirm_exit:
                console.print(Text("Exiting the tool...", style="red"))
                exit(0)
    except Exception as e:
        console.print(f"Error occurred: {e}", style="red")


def MainMenu():
    '''renders the main menu using inquirer''' 
    try:
        menuPrompt = [inquirer.List('menuChoice', message='What would you like to do?', choices=MENU_CHOICES)]
        choice = inquirer.prompt(menuPrompt)
        if not choice or 'menuChoice' not in choice:
            console.print(Text("Invalid selection. Please try again.", style="red"))
            return
        handleMenuChoice(choice['menuChoice'])
    except Exception as e:
        console.print(f"Error: {e}", style="red")


def main():
    '''main function'''
    while True:
        try:
            DisplayTitle()
            MainMenu()
        except KeyboardInterrupt:
            console.print(Text("\nExiting the tool...", style="red2"))
            break


# run
if __name__ == '__main__':
    main()
