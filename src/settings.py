import inquirer
import os
from dotenv import load_dotenv, set_key
from rich.console import Console
from rich.text import Text
import json
from .encryption import DecryptPassword
from .encryption import SavePassword

console = Console()


def ConsolePrint(message, color="white"):
    '''prints a message to the console with a specified color'''
    global consolePrintCount
    console.print(Text(message, style=color), end='')
    consolePrintCount += 1


def ClearConsole():
    '''clears the console'''
    global consolePrintCount
    print('\033[A\033[K' * consolePrintCount, end='')
    consolePrintCount = 0


def setJsonAttribute(attribute, value):
    '''will rewrite the settings.json'''
    with open('data/settings.json', 'r') as file:
        data = json.load(file)
    data[attribute] = value
    with open('data/settings.json', 'w') as file:
        json.dump(data, file)
    file.close()


def FixPasswordLength(toFix):
    '''displays the menu for customize password'''
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
        console.print(Text('\nPassword length will be asked every time', style='green'))

    input()


def RewritePasswords(key, newKey):
    '''will write the new encrypted passwords data'''
    with open('./data/passwords.enc', 'r') as file:
        lines = file.readlines()
    with open('./data/passwords.enc', 'w') as file:
        file.truncate(0)
    
    for line in lines:
        website, username, password = line.strip().split('\t')
        decryptedPassword = DecryptPassword(password, key)
        SavePassword(newKey, decryptedPassword, website, username, True)


def ChangeMasterKey():
    '''change master key logic'''
    load_dotenv()

    while True:
        console.print(Text('Enter the Master Key: '), style='cyan', end='')
        key = input()
        
        if key == '':
            print('\033[A\033[K' * 1, end='')
            console.print(Text('Master Key cannot be empty!', style='red'), end='\n')
        elif key != os.getenv('MASTER_KEY'):
            print('\033[A\033[K' * 1, end='')
            console.print(Text('Invalid Master Key!', style='red'), end='\n')
        else:
            break

    console.print(Text('Enter the new Master Key: '), style='cyan', end='')
    newKey = input()

    set_key('.env', 'MASTER_KEY', newKey)
    RewritePasswords(key, newKey)

    console.print(Text('\nMaster Key changed successfully!', style='green'), end='\n')
    exit(0)


def EraseData():
    '''erases all the data'''
    while True:
        console.print(Text('Enter the Master Key: '), style='cyan', end='')
        key = input()
        
        if key == '':
            print('\033[A\033[K' * 1, end='')
            console.print(Text('Master Key cannot be empty!', style='red'), end='\n')
        elif key != os.getenv('MASTER_KEY'):
            print('\033[A\033[K' * 1, end='')
            console.print(Text('Invalid Master Key!', style='red'), end='\n')
        else:
            break

    question = [
        inquirer.Confirm(
            'confirm',
            message='Are you sure you want to erase all the data?',
            default=False
        )
    ]
    answer = inquirer.prompt(question)
    if (answer['confirm']):
        with open('./data/passwords.enc', 'w') as file:
            file.truncate(0)
        console.print(Text('Data Erased Successfully!', style='green'), end='\n')
        input();
 


# main function
def settings():
    print('\033[A\033[K' * 6, end='')
    with open('./data/settings.json', 'r') as file:
        settings_data = json.load(file)
    
    default_force = settings_data.get('defaultForce', False)
    password_status = 'Fix Password Length' if not default_force else 'Unfix Password Length'

    menuChoicesList = [
        password_status,
        'Change the Master Key',
        'Erase All Data',
        'Back'
    ]

    mainMenu = [inquirer.List('menuChoice',
                            message='Settings',
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
    