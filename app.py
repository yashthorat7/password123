from inquirer import List, confirm, prompt
from rich.console import Console
from rich.text import Text
from src.display_title import display_title

console = Console()

class MenuHandler:
    MENU_CHOICES = [
        "Generate a Password",
        "Display the Passwords",
        "Settings",
        "Exit",
    ]

    @staticmethod
    def clear_lines(lines):
        print('\033[A\033[K' * lines, end='')

    @staticmethod
    def handle_choice(choice):
        if choice == "Generate a Password":
            pass
        elif choice == "Display the Passwords":
            pass
        elif choice == "Settings":
            pass
        elif choice == "Exit":
            if confirm("Exit the program?", default=True):
                console.print(Text("Exited...", style="red"))
                console.print(Text("made by Yash Thorat", style="red"))
                exit(0)

    def render_menu(self):
        menu_prompt = [List("menuChoice", message="What would you like to do?", choices=self.MENU_CHOICES)]
        choice = prompt(menu_prompt).get("menuChoice")
        if choice:
            self.handle_choice(choice)

def main():
    menu_handler = MenuHandler()
    while True:
        display_title()
        menu_handler.render_menu()

if __name__ == "__main__":
    main()