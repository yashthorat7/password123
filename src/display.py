import os
import inquirer
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED
from .encryption import DecryptPassword, SavePassword

console = Console()
load_dotenv()
tableClone = []
PASSWORD_FILE = 'data/passwords.enc'


def GetMasterKey():
    '''authenticates using master key'''
    console.print(Text('Enter the Master Key: ', style='cyan'), end='')
    key = input()
    if not key:
        console.print(Text('Master Key cannot be empty!', style='red'), end='\n')
        return False, None
    if key != os.getenv('MASTER_KEY'):
        console.print(Text('Invalid Master Key!', style='red'), end='\n')
        return False, None
    return True, key


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
    for header, style in zip(headers, styles):
        table.add_column(header, justify='left', style=style)
    for row in rows:
        table.add_row(*row)
    return table


def DisplayTable(key):
    '''displays the table'''
    try:
        global tableClone
        tableClone = []
        lines = ReadPasswords()
        rows = []
        for i, line in enumerate(lines, start=1):
            columns = line.strip().split('\t')
            if len(columns) == 3:
                website, username, password = columns
                decryptedPassword = DecryptPassword(password, key)
                rows.append([str(i), website, username, decryptedPassword])
                tableClone.append([str(i), website, username, decryptedPassword])
        if not tableClone:
            console.print(Text('No Data found', style='red'))
            return False
        table = CreateTable(['Sr.no.', 'Website', 'Username', 'Password'], rows, ['orange3', 'purple', 'red', 'yellow'])
        console.print(table)
        return True
    except Exception as e:
        console.print(Text(f'Error displaying table: {e}', style='red'))
        return False


def HandleSearch():
    '''search logic for the table'''
    console.print(Text('Enter the Website: ', style='cyan'), end='')
    website = input()
    matchedRows = [row for row in tableClone if row[1].lower() == website.lower()]
    if matchedRows:
        table = CreateTable(['Sr.no.', 'Username', 'Password'], matchedRows, ['yellow', 'red', 'magenta'])
        console.print(table)
    else:
        console.print(Text('No match found', style='red'))


def HandleAdd():
    '''add logic for the table'''
    try:
        SavePassword(os.getenv('MASTER_KEY'))
    except Exception as e:
        console.print(Text(f'Error adding password: {e}', style='red'))


def HandleRemove():
    '''delete logic for the table'''
    try:
        console.print(Text('Enter the serial No: ', style='cyan'), end='')
        rowIndex = int(input()) - 1
        if 0 <= rowIndex < len(tableClone):
            table = CreateTable(['Sr.no.', 'Website', 'Username', 'Password'], [tableClone[rowIndex]], ['yellow', 'red', 'magenta', 'red'])
            console.print(table)
            confirmChoice = inquirer.prompt([inquirer.Confirm('confirm', message='Are you sure you want to remove this password?', default=False)])['confirm']
            if confirmChoice:
                lines = ReadPasswords()
                del lines[rowIndex]
                WritePasswords(lines)
                console.print(Text('Password removed successfully\n', style='yellow'))
            else:
                console.print(Text('Operation cancelled\n', style='cyan'))
        else:
            console.print(Text('Invalid serial number', style='red'))
    except ValueError:
        console.print(Text('Please enter a valid number', style='red'))
    except Exception as e:
        console.print(Text(f'Error removing password: {e}', style='red'))


def DisplayMenu(key):
    '''renders the display menu using inquirer'''
    while True:
        if not DisplayTable(key):
            break
        menuChoice = inquirer.prompt([inquirer.List('menuChoice', message='What would you like to do?', choices=[
            'Search a Password', 'Add a Password', 'Remove a Password', 'Back'])])['menuChoice']
        if menuChoice == 'Search a Password':
            HandleSearch()
        elif menuChoice == 'Add a Password':
            HandleAdd()
        elif menuChoice == 'Remove a Password':
            HandleRemove()
        elif menuChoice == 'Back':
            break


# main function
def display():
    try:
        for _ in range(3):
            validKey, key = GetMasterKey()
            if validKey:
                DisplayMenu(key)
                return
    except Exception as e:
        console.print(Text(f'Unexpected error: {e}', style='red'))
