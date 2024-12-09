import inquirer
import os
from rich.console import Console
from rich.text import Text
import json

console = Console()


def setJsonAttribute(attribute, value):
    with open('./data/settings.json', 'r') as file:
        data = json.load(file)
    data[attribute] = value
    with open('./data/settings.json', 'w') as file:
        json.dump(data, file)
    file.close()


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
                          default=['Uppercase Letters', 'Lowercase Letters', 'Numbers', 'Special Characters']
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
                    setJsonAttribute('defaultForceNum', length)
                    setJsonAttribute('defaultForce', True)
                    console.print(Text(f'Password length set to {length} forever', style='green'))
                    break
            except ValueError:
                console.print(Text('Please enter a valid number', style='red'))
    else:
        setJsonAttribute('defaultForce', False)
        console.print(Text('Password length will be asked everytime', style='green'))

    if 'Special Characters' in userChoices:
        setJsonAttribute('specialCharacters', True)
        console.print(Text('Included special characters from password', style='green'))
    else:
        setJsonAttribute('specialCharacters', False)
        console.print(Text('Removed special characters from password', style='green'))

    if 'Numbers' in userChoices:
        setJsonAttribute('numbers', True)
        console.print(Text('Included numbers from password', style='green'))
    else:
        setJsonAttribute('numbers', False)
        console.print(Text('Removed numbers from password', style='green'))

    if 'Uppercase Letters' in userChoices:
        setJsonAttribute('uppercase', True) 
        console.print(Text('Included uppercase letters from password', style='green'))
    else:
        setJsonAttribute('uppercase', False)
        console.print(Text('Removed uppercase letters from password', style='green'))

    if 'Lowercase Letters' in userChoices:
        setJsonAttribute('lowercase', True)
        console.print(Text('Included lowercase letters from password', style='green'))
    else:
        setJsonAttribute('lowercase', False)
        console.print(Text('Removed lowercase letters from password', style='green'))

    print('')


def ChangeMasterKey():
    pass


def EraseData():
    while True:
        console.print(Text('Enter the Master Key: '), style='cyan', end='')
        key = input()
        
        if (key == ''):
            console.print(Text('Master Key cannot be empty!', style='red'), end='\n')
        elif (key != os.getenv('MASTER_KEY')):
            console.print(Text('Invalid Master Key!', style='red'), end='\n')
        else:
            break

    with open('./data/passwords.json', 'w') as file:
        file.truncate(0)
    file.close()
    console.print(Text('Data Erased Successfully!', style='green'), end='\n')


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
    