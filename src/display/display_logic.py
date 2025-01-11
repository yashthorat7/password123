import json
import inquirer
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED
from ..encryption import DecryptPassword, SavePassword
from .display_table import console_print, clear_console, paginate_table

console = Console()
consolePrintCount = 0
tableClone = []
PASSWORD_FILE = 'data/passwords.enc'
SETTINGS_FILE = 'data/settings.json'
masterKeyGlobal = None


def GetMasterKey():
    try:
        with open(SETTINGS_FILE, 'r') as file:
            settings = json.load(file)
            global masterKeyGlobal
            masterKeyGlobal = settings['masterKey']
            return True
    except Exception as e:
        console_print(f'Error loading master key: {e}', 'red')
        return False


def ReadPasswords():
    with open(PASSWORD_FILE, 'r') as file:
        return file.readlines()


def WritePasswords(lines):
    with open(PASSWORD_FILE, 'w') as file:
        file.writelines(lines)


def DisplayTable():
    try:
        global tableClone
        lines = ReadPasswords()
        rows = []
        for i, line in enumerate(lines, start=1):
            columns = line.strip().split('\t')
            if len(columns) == 3:
                website, username, password = columns
                decryptedPassword = DecryptPassword(password, masterKeyGlobal)
                rows.append([str(i), website, username, decryptedPassword])
                tableClone.append([str(i), website, username, decryptedPassword])
        if not tableClone:
            console_print('No Data found', 'red')
            return False
        paginate_table(['Sr.no.', 'Website', 'Username', 'Password'], rows, ['orange3', 'cyan', 'red', 'yellow'])
        return True
    except Exception as e:
        console_print(f'Error displaying table: {e}', 'red')
        return False


def HandleSearch():
    console_print('Enter the Website: ', 'cyan')
    website = input()
    website = 'N/A' if website == '' else website
    matchedRows = [row for row in tableClone if row[1].lower() == website.lower()]
    print('\033[A\033[K' * 1, end='')
    clear_console()
    if matchedRows:
        paginate_table(['Sr.no.', 'Website', 'Username', 'Password'], matchedRows, ['orange3', 'cyan', 'red', 'yellow'])
    else:
        console_print('No match found', 'red')


def HandleAdd():
    try:
        SavePassword(masterKeyGlobal)
        print('\033[A\033[K' * 8, end='')
        clear_console()
    except Exception as e:
        console_print(f'Error adding password: {e}', 'red')


def HandleRemove():
    try:
        console_print('Enter the serial No: ', 'cyan')
        rowIndex = int(input()) - 1
        if 0 <= rowIndex < len(tableClone):
            table = paginate_table(['Sr.no.', 'Website', 'Username', 'Password'], [tableClone[rowIndex]], ['yellow', 'red', 'magenta', 'red'])
            console.print(table)
            confirmChoice = inquirer.prompt([inquirer.Confirm('confirm', message='Are you sure you want to remove this password?', default=False)])['confirm']
            if confirmChoice:
                lines = ReadPasswords()
                del lines[rowIndex]
                WritePasswords(lines)
                console_print('Password removed successfully\n', 'yellow')
            else:
                console_print('Operation cancelled\n', 'cyan')
        else:
            console_print('Invalid serial number', 'red')
        print('\033[A\033[K' * 11, end='')
        clear_console()
    except ValueError:
        console_print('Please enter a valid number', 'red')
    except Exception as e:
        console_print(f'Error removing password: {e}', 'red')


def DisplayMenu():
    while True:
        try:
            menuChoice = inquirer.prompt([inquirer.List('menuChoice', 
                message='What would you like to do?', 
                choices=['Search a Password', 'Add a Password', 'Remove a Password', 'Back']
            )])
            if not menuChoice:  # Handle Ctrl+C
                return False
                
            choice = menuChoice['menuChoice']
            print('\033[A\033[K' * 5, end='')
            
            if choice == 'Search a Password':
                HandleSearch()
            elif choice == 'Add a Password':
                HandleAdd()
            elif choice == 'Remove a Password':
                HandleRemove()
            elif choice == 'Back':
                return False
            return True
            
        except Exception as e:
            console_print(f'Menu error: {e}', 'red')
            return False

# run
def display():
    try:
        validKey = GetMasterKey()
        clear_console()
        while validKey:
            DisplayTable()
            if not DisplayMenu():
                clear_console()
                return
            clear_console()
    except Exception as e:
        console_print(f'Unexpected error: {e}', 'red')
