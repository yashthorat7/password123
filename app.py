import inquirer
from rich.console import Console
from rich.text import Text
from src.generator import generator
from src.display import display
from src.settings import settings

console = Console()

TITLE_TEXT = [
    ('#ff5ca8', r' ____   _    ____ ______        _____  ____  ____  _ ____  _____ '),
    ('#ff70a1', r'|  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \/ |___ \|___ / '),
    ('#ff8c8b', r'| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | | | __) | |_ \ '),
    ('#ffa168', r'|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| | |/ __/ ___) |'),
    ('#ffa724', r'|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/|_|_____|____/ '),
]

MENU_CHOICES = [
    'Generate a Password',
    'Display the Passwords',
    'Settings',
    'Exit'
]


# displays the title text
def DisplayTitle():
    for color, line in TITLE_TEXT:
        styledTitle = Text(line, style=color)
        console.print(styledTitle)
    console.print('')


# calls function according to the user's choice
def handleMenuChoice(userChoice):
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
                console.print("Exiting the tool...", style="orange3")
                exit(0)
    except Exception as e:
        console.print(f"Error occurred: {e}", style="red")


# renders the main menu using inquirer
def MainMenu():
    try:
        menuPrompt = [inquirer.List('menuChoice', message='What would you like to do?', choices=MENU_CHOICES)]
        choice = inquirer.prompt(menuPrompt)
        if not choice or 'menuChoice' not in choice:
            console.print("Invalid selection. Please try again.", style="bold red")
            return
        handleMenuChoice(choice['menuChoice'])
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


# main function
def main():
    DisplayTitle()
    while True:
        try:
            MainMenu()
        except KeyboardInterrupt:
            console.print("\nExiting the tool. Goodbye!", style="orange3")
            break


# run
if __name__ == '__main__':
    main()
