import json
import inquirer
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED
from .encryption import DecryptPassword, SavePassword

console = Console()
consolePrintCount = 0
tableClone = []
PASSWORD_FILE = 'data/passwords.enc'
SETTINGS_FILE = 'data/settings.json'
# masterKeyGlobal = ''
masterKeyGlobal = 'IamBatman'


def ConsolePrint(message='', color="white", iend=''):
    '''prints a message to the console with a specified color'''
    global consolePrintCount
    console.print(Text(message, style=color), end=iend)
    consolePrintCount += 1


def ClearConsole():
    '''clears the console'''
    global consolePrintCount
    print('\033[A\033[K' * consolePrintCount, end='')
    consolePrintCount = 0


def GetMasterKey():
    '''authenticates using master key'''
    with open(SETTINGS_FILE, 'r') as file:
        settings = json.load(file)
        masterKey = settings.get('masterKey', '')
        global masterKeyGlobal
        masterKeyGlobal = masterKey
    for _ in range(5):
        ConsolePrint('Enter the Master Key: ', 'cyan')
        key = input()
        if not key:
            ClearConsole()
            ConsolePrint('Master Key cannot be empty!', 'red', '\n')
        elif key != masterKey:
            ClearConsole()
            ConsolePrint('Invalid Master Key!', 'red', '\n')
        if key == masterKey:
            return True, key
    return False, ''


def ReadPasswords():
    '''will open the passwords.enc'''
    with open(PASSWORD_FILE, 'r') as file:
        return file.readlines()


def WritePasswords(lines):
    '''will write the passwords.enc'''
    with open(PASSWORD_FILE, 'w') as file:
        file.writelines(lines)


def CreateTable(headers, rows, styles):
    '''creates a table using rich table'''
    table = Table(header_style='bold', box=ROUNDED)
    global consolePrintCount
    consolePrintCount += 5
    for header, style in zip(headers, styles):
        table.add_column(header, justify='left', style=style)
        consolePrintCount += 1
    for row in rows:
        table.add_row(*row)
        consolePrintCount += 1
    return table


def DisplayTable():
    '''displays the table'''
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
            ConsolePrint('No Data found', 'red')
            return False
        table = CreateTable(['Sr.no.', 'Website', 'Username', 'Password'], rows, ['orange3', 'cyan', 'red', 'yellow'])
        console.print(table)
        return True
    except Exception as e:
        ConsolePrint(f'Error displaying table: {e}', 'red')
        return False


def HandleSearch():
    '''search logic for the table'''
    ConsolePrint('Enter the Website: ', 'cyan')
    website = input()
    website = 'N/A' if website == '' else website
    matchedRows = [row for row in tableClone if row[1].lower() == website.lower()]
    if matchedRows:
        table = CreateTable(['Sr.no.', 'Website', 'Username', 'Password'], matchedRows, ['orange3', 'cyan', 'red', 'yellow'])
        console.print(table)
        input()
        print('\033[A\033[K' * (len(matchedRows) + 7), end='')
    else:
        ConsolePrint('No match found', 'red')
        input()
        print('\033[A\033[K' * 3, end='')


def HandleAdd():
    '''add logic for the table'''
    try:
        SavePassword(masterKeyGlobal)
        ClearConsole()
        print('\033[A\033[K' * 7, end='')
        DisplayTable(masterKeyGlobal)
    except Exception as e:
        ConsolePrint(f'Error adding password: {e}', 'red')


def HandleRemove():
    '''delete logic for the table'''
    try:
        ConsolePrint('Enter the serial No: ', 'cyan')
        rowIndex = int(input()) - 1
        if 0 <= rowIndex < len(tableClone):
            table = CreateTable(['Sr.no.', 'Website', 'Username', 'Password'], [tableClone[rowIndex]], ['yellow', 'red', 'magenta', 'red'])
            ConsolePrint(table)
            confirmChoice = inquirer.prompt([inquirer.Confirm('confirm', message='Are you sure you want to remove this password?', default=False)])['confirm']
            if confirmChoice:
                lines = ReadPasswords()
                del lines[rowIndex]
                WritePasswords(lines)
                ConsolePrint('Password removed successfully\n', 'yellow')
            else:
                ConsolePrint('Operation cancelled\n', 'cyan')
        else:
            ConsolePrint('Invalid serial number', 'red')
    except ValueError:
        ConsolePrint('Please enter a valid number', 'red')
    except Exception as e:
        ConsolePrint(f'Error removing password: {e}', 'red')


def DisplayMenu():
    '''renders the display menu using inquirer'''
    while True:
        menuSize = 5
        menuChoice = inquirer.prompt([inquirer.List('menuChoice', message='What would you like to do?', choices=[
            'Search a Password', 'Add a Password', 'Remove a Password', 'Back'])])['menuChoice']
        if menuChoice == 'Search a Password':
            print('\033[A\033[K' * menuSize, end='')
            HandleSearch()
        elif menuChoice == 'Add a Password':
            HandleAdd()
        elif menuChoice == 'Remove a Password':
            HandleRemove()
        elif menuChoice == 'Back':
            break


# run
def display():
    try:
        # validKey, key = GetMasterKey()
        validKey, key = True, 'IamBatman'
        if validKey:
            ClearConsole()
            DisplayTable()
            DisplayMenu()
            ClearConsole()
            return
        ClearConsole()
    except Exception as e:
        ConsolePrint(f'Unexpected error: {e}', 'red')
