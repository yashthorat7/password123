import inquirer
from rich.console import Console
from rich.text import Text
from src.generator import generator
from src.display import display
from src.settings import settings

console = Console()


# disply the banner
def DisplayTitle():
    titleText = [
        ('#ff5ca8', r' ____   _    ____ ______        _____  ____  ____  _ ____  _____ '),
        ('#ff70a1', r'|  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \/ |___ \|___ / '),
        ('#ff8c8b', r'| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | | | __) | |_ \ '),
        ('#ffa168', r'|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| | |/ __/ ___) |'),
        ('#ffa724', r'|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/|_|_____|____/ '),
    ]

    for color, line in titleText:
        styledTitle = Text(line, style=color)
        console.print(styledTitle)
    print('')

# main menu
def main():
    userChoicesList = [
        'Generate a Password',
        'Display the Passwords',
        'Settings',
        'Exit'
    ]

    mainMenu = [inquirer.List('menuChoice',
                             message='What would you like to do?',
                             choices=userChoicesList,
                )]

    menuChoice = inquirer.prompt(mainMenu)
    userChoice = menuChoice['menuChoice']

    if userChoice == 'Generate a Password':
        generator()
    elif userChoice == 'Display the Passwords':
        display()
    elif userChoice == 'Settings':
        settings()
    elif userChoice == 'Exit':
        console.print('Tool Exited..', style='yellow')
        exit(0)


if __name__ == '__main__':
    DisplayTitle()
    while True:
        main()
