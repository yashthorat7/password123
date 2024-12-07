import random
import string
import inquirer
from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.panel import Panel
from rich.box import ROUNDED
from .encryption import SavePassword

console = Console()


# generates a password...need to change
def GeneratePassword(passwordLength):
    characters = string.ascii_letters + string.digits + string.punctuation
    Password = ''.join(random.choice(characters) for i in range(passwordLength))

    return Password


# used rich panel to show password in a box
def DisplayPassword(password):
    passwordText = Text('Generated Password: ', style='green') + Text(password, style='cyan')

    passwordContainer = Panel(passwordText, style='bold', expand=False, box=ROUNDED)
    console.print(passwordContainer)
    print('')


#jumps to the encryption.py if true
def AskSave(password):
    menuChoicesList = [
        'Yes',
        'No',
        'Generate Again'
    ]

    mainMenu = [inquirer.List('menuChoice',
                            message='Save the password?',
                            choices=menuChoicesList,
                )]

    menuChoice = inquirer.prompt(mainMenu)
    userChoice = menuChoice['menuChoice']
    
    if userChoice == 'Yes':
        SavePassword(password)
    elif userChoice == 'No':
        return
    else:
        generator()


# asks the length of the password and validates it
def getPasswordLength():
    validLength = False

    while not validLength:
        DEFAULT_LENGTH, MIN_LENGTH, MAX_LENGTH = 12, 8, 64

        console.print(Text('Enter the length of the password ', style='yellow') + Text(f'(default={DEFAULT_LENGTH})', style='orange3') + Text(': ', style='yellow'), end='')
        length = input()
        
        if length == '':
            passwordLength = 12
            validLength = True
        else:
            try:
                passwordLength = int(length)
            except ValueError:
                console.print('Please enter a valid number', style='red')
                continue
            
            if passwordLength < MIN_LENGTH:
                console.print(f'Password must be at least {MIN_LENGTH} characters long', style='red')
            elif passwordLength > MAX_LENGTH:
                console.print(f'Password must be at most {MAX_LENGTH} characters long', style='red')
            else:
                validLength = True

    return passwordLength


# main function
def generator():
    passwordLength = getPasswordLength()
    newPassword = GeneratePassword(passwordLength)
    DisplayPassword(newPassword)
    AskSave(newPassword)
    