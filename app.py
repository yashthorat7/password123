import inquirer
from rich.console import Console
from rich.text import Text
from src.generator import generator
from src.display import display
from src.settings import settings

# disply the banner
def DisplayTitle():
    titleText = (r'''
                  ____   _    ____ ______        _____  ____  ____  _ ____  _____ 
|  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \/ |___ \|___ / 
| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | | | __) | |_ \ 
|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| | |/ __/ ___) |
|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/|_|_____|____/ 
''')
    console = Console()
    styledTitle = Text(titleText, style='bold yellow')
    console.print(styledTitle)

# main menu
def main():
    menuChoicesList = [
        'Generate a Password',
        'Display the Passwords',
        'Settings',
        'Exit'
    ]

    # console = Console()
    mainMenu = [inquirer.List('menuChoice',
                             message='What would you like to do?',
                             choices=menuChoicesList,
                )]

    userChoice = inquirer.prompt(mainMenu)
    menuChoice = userChoice['menuChoice']

    if menuChoice == 'Generate a Password':
        generator()
    elif menuChoice == 'Display the Passwords':
        display()
    elif menuChoice == 'Settings':
        settings()
    elif menuChoice == 'Exit':
        print('Program Exited')
        exit(0)


if __name__ == '__main__':
    DisplayTitle()
    while True:
        main()
