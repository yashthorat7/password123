from inquirer import List, confirm, prompt
from rich.console import Console
from rich.text import Text
from src.display_title import display_title

console = Console()

MENU_CHOICES = [
    "Generate a Password",
    "Display the Passwords",
    "Settings",
    "Exit",
]

def clear_lines(lines):
    print('\033[A\033[K' * lines, end='')

def handle_choice(choice):
    if choice == "Generate a Password":
        pass
    elif choice == "Display the Passwords":
        pass
    elif choice == "Settings":
        pass
    elif choice == "Exit":
        if confirm("Exit the program?", default=True):
            clear_lines(2)
            console.print(Text("Exited...", style="red"))
            console.print(Text("--coded by Yash Thorat", style="red"))
            exit(0)

def render_menu():
    menu_prompt = [List("menuChoice", message="Main Menu", choices=MENU_CHOICES)]
    choice = prompt(menu_prompt).get("menuChoice")
    if choice:
        handle_choice(choice)

def main():
    while True:
        display_title()
        render_menu()

if __name__ == "__main__":
    main()