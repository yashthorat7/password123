import inquirer
import os
from dotenv import load_dotenv, set_key
from rich.console import Console
from rich.text import Text
import json
from .encryption import DecryptPassword
from .encryption import SavePassword

console = Console()


# will rewrite the settings.json
def setJsonAttribute(attribute, value):
    with open('data/settings.json', 'r') as file:
        data = json.load(file)
    data[attribute] = value
    with open('data/settings.json', 'w') as file:
        json.dump(data, file)
    file.close()


# displays the menu for customize password
def FixPasswordLength(toFix):
    with open('data/settings.json', 'r') as file:
        data = json.load(file)

    if toFix:
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
        console.print(Text('Password length will be asked every time', style='green'))

    print('')


# will write the new encrypted passwords data
def RewritePasswords(key, newKey):
    with open('./data/passwords.enc', 'r') as file:
        lines = file.readlines()
    with open('./data/passwords.enc', 'w') as file:
        file.truncate(0)
    
    for line in lines:
        website, username, password = line.strip().split('\t')
        decryptedPassword = DecryptPassword(password, key)
        SavePassword(newKey, decryptedPassword, website, username, True)


# change master key logic
def ChangeMasterKey():
    load_dotenv()

    while True:
        console.print(Text('Enter the Master Key: '), style='cyan', end='')
        key = input()
        
        if key == '':
            console.print(Text('Master Key cannot be empty!', style='red'), end='\n')
        elif key != os.getenv('MASTER_KEY'):
            console.print(Text('Invalid Master Key!', style='red'), end='\n')
        else:
            break

    console.print(Text('Enter the new Master Key: '), style='cyan', end='')
    newKey = input()

    set_key('.env', 'MASTER_KEY', newKey)
    RewritePasswords(key, newKey)

    console.print(Text('Master Key changed successfully!', style='green'), end='\n')
    exit(0)


# erases all the data
def EraseData():
    while True:
        console.print(Text('Enter the Master Key: '), style='cyan', end='')
        key = input()
        
        if key == '':
            console.print(Text('Master Key cannot be empty!', style='red'), end='\n')
        elif key != os.getenv('MASTER_KEY'):
            console.print(Text('Invalid Master Key!', style='red'), end='\n')
        else:
            break

    mainMenu = [inquirer.List('menuChoice',
                            message='Save the password?',
                            choices=['Yes', 'No'],
                )]

    menuChoice = inquirer.prompt(mainMenu)
    userChoice = menuChoice['menuChoice']
    
    if userChoice == 'Yes':
        with open('./data/passwords.enc', 'w') as file:
            file.truncate(0)
        file.close()
        console.print(Text('Data Erased Successfully!', style='green'), end='\n')
        print('')


# main function
def settings():
    with open('./data/settings.json', 'r') as file:
        settings_data = json.load(file)
    
    default_force = settings_data.get('defaultForce', False)
    password_status = "Fix Password Length" if not default_force else "Unfix Password Length"

    menuChoicesList = [
        password_status,
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

    if userChoice == 'Fix Password Length':
        FixPasswordLength(True)
    elif userChoice == 'Unfix Password Length':
        FixPasswordLength(False)
    elif userChoice == 'Change the Master Key':
        ChangeMasterKey()
    elif userChoice == 'Erase All Data':
        EraseData()
    else:
        pass
    