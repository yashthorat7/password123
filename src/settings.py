import inquirer
from rich.console import Console
from rich.text import Text
import json

console = Console()

def CustomizePassword():
    settingsChoicesList = [
        'Length of Password',
        'Special Characters',
        'Numbers',
        'Uppercase Letters',
        'Lowercase Letters'
    ]

    settingsMenu = [inquirer.Checkbox('settings',
                          message='What would you like to change?',
                          choices=settingsChoicesList,
                          default=['Length of Password','Uppercase Letters', 'Lowercase Letters']
                    )]

    userChoices = inquirer.prompt(settingsMenu)['settings']

    if 'Length of Password' in userChoices:
        while True:
            console.print(Text('Enter a fixed length: ', style='cyan'), end='')
            length = input()
            try:
                length = int(length)
                if length < 8:
                    console.print(Text('Password must be at least 8 characters long', style='red'))
                elif length > 64:
                    console.print(Text('Password must be at most 64 characters long', style='red'))
                else:
                    with open('./data/settings.json', 'r') as file:
                        data = json.load(file)
                    data['default'] = length
                    data['defaultforce'] = True
                    with open('./data/settings.json', 'w') as file:
                        json.dump(data, file)

                    console.print(Text(f'Password length set to {length} forever'), style='green')
                    break
            except ValueError:
                console.print('Please enter a valid number', style='red')

    elif 'Special Characters' in userChoices:
        pass
    elif 'Numbers' in userChoices:
        pass
    elif 'Uppercase Letters' in userChoices:
        pass
    elif 'Lowercase Letters' in userChoices:
        pass
    else:
        pass


def ChangeMasterKey():
    pass


def EraseData():
    pass


# main function
def settings():
    menuChoicesList = [
        'Customize Password',
        'Change the Master Key',
        'Erase All Data',
        'Back'
    ]

    mainMenu = [inquirer.List('menuChoice',
                            message='What would you like to do?',
                            choices=menuChoicesList,
                )]

    menuChoice = inquirer.prompt(mainMenu)
    userChoice = menuChoice['menuChoice']

    if userChoice == 'Customize Password':
        CustomizePassword()
    elif userChoice == 'Change the Master Key':
        ChangeMasterKey
    elif userChoice == 'Erase All Data':
        EraseData()
    else:
        pass
    