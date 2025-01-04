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
masterKeyGlobal = None


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
    '''Get master key from settings and store globally'''
    try:
        with open(SETTINGS_FILE, 'r') as file:
            settings = json.load(file)
            global masterKeyGlobal
            masterKeyGlobal = settings['masterKey']
            return True
    except Exception as e:
        ConsolePrint(f'Error loading master key: {e}', 'red')
        return False


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
    for row in rows:
        consolePrintCount += 1
        table.add_row(*row)
    return table


def PaginateTable(headers, rows, styles):
    '''paginates table rows with inquirer menu'''
    page_size = 10
    current_page = 0
    total_pages = (len(rows) + page_size - 1) // page_size
    global consolePrintCount

    while True:
        start_index = current_page * page_size
        end_index = start_index + page_size
        table = CreateTable(headers, rows[start_index:end_index], styles)

        console.print(table)
        ConsolePrint(f'\t\t\tPage {current_page + 1} of {total_pages}', 'cyan', '\n')

        if total_pages == 1:
            return

        choices = []
        if current_page > 0:
            choices.append("Previous")
        if current_page < total_pages - 1:
            choices.append("Next")
        choices.append("Menu")

        consolePrintCount += len(choices) + 1
        action = inquirer.prompt([
            inquirer.List('action', message='Navigate pages', choices=choices)
        ])['action']

        if action == "Next": 
            ClearConsole()
            current_page += 1
        elif action == "Previous":
            ClearConsole()
            current_page -= 1
        elif action == "Menu":
            menuSize = len(choices) + 3
            consolePrintCount -= menuSize
            print('\033[A\033[K' * menuSize, end='')
            break


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
        PaginateTable(['Sr.no.', 'Website', 'Username', 'Password'], rows, ['orange3', 'cyan', 'red', 'yellow'])
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
    print('\033[A\033[K' * 1, end='')
    ClearConsole()
    if matchedRows:
        PaginateTable(['Sr.no.', 'Website', 'Username', 'Password'], matchedRows, ['orange3', 'cyan', 'red', 'yellow'])
    else:
        ConsolePrint('No match found', 'red')


def HandleAdd():
    '''add logic for the table'''
    try:
        SavePassword(masterKeyGlobal)
        print('\033[A\033[K' * 8, end='')
        ClearConsole()
    except Exception as e:
        ConsolePrint(f'Error adding password: {e}', 'red')


def HandleRemove():
    '''delete logic for the table'''
    try:
        ConsolePrint('Enter the serial No: ', 'cyan')
        rowIndex = int(input()) - 1
        if 0 <= rowIndex < len(tableClone):
            table = CreateTable(['Sr.no.', 'Website', 'Username', 'Password'], [tableClone[rowIndex]], ['yellow', 'red', 'magenta', 'red'])
            console.print(table)
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
        print('\033[A\033[K' * 11, end='')
        ClearConsole()
    except ValueError:
        ConsolePrint('Please enter a valid number', 'red')
    except Exception as e:
        ConsolePrint(f'Error removing password: {e}', 'red')


def DisplayMenu():
    '''renders the display menu using inquirer'''
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
            ConsolePrint(f'Menu error: {e}', 'red')
            return False

# run
def display():
    try:
        validKey = GetMasterKey()
        ClearConsole()
        while validKey:
            DisplayTable()
            if not DisplayMenu():
                ClearConsole()
                return
            ClearConsole()
    except Exception as e:
        ConsolePrint(f'Unexpected error: {e}', 'red')
