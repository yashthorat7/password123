from rich.console import Console
from rich.text import Text
from src.generator import generator
from src.display import display
from src.settings import settings


def DisplayTitle():
    titleText = (r''' ____   _    ____ ______        _____  ____  ____  _ ____  _____ 
|  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \/ |___ \|___ / 
| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | | | __) | |_ \ 
|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| | |/ __/ ___) |
|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/|_|_____|____/ 
''')
    console = Console()
    styledTitle = Text(titleText, style='bold yellow')
    console.print(styledTitle)


# TODO: menu should be interactive
def main(): 
    print('--------------------------------------------')
    print('1. Generate a Password')
    print('2. Saved Passwords')
    print('3. Settings')
    print('4. Exit')
    choice = input('Enter a choice: ')

    if choice == '1':
        generator()
    elif choice == '2':
        display()
    elif choice == '3':
        settings()
    elif choice == '4':
        exit(0)
    else:
        print('Invalid choice')


if __name__ == '__main__':
    DisplayTitle()
    while True:
        main()
