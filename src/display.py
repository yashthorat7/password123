import os
import inquirer
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED
from .encryption import DecryptPassword
from .encryption import SavePassword

console = Console()
load_dotenv()
tableClone = []


# checks if the master key is correct
def getMasterKey():
    console.print(Text('Enter the Master Key: '), style='cyan', end='')
    key = input()
    
    if (key == ''):
        console.print(Text('Master Key cannot be empty!', style='red'), end='\n')
    elif (key != os.getenv('MASTER_KEY')):
        console.print(Text('Invalid Master Key!', style='red'), end='\n')

    return key == os.getenv('MASTER_KEY'), key


# searches the table clone and filters the outputs
def SearchRow():
    console.print(Text('Enter the Website: '), style='cyan', end='')
    website = input()
    matchedRows = []

    for row in tableClone:
        if row[1] == website:
            matchedRows.append(row)

    if matchedRows:
        table = Table(header_style='bold', box=ROUNDED)
        table.add_column('Sr.no.', justify='left', style='yellow')
        table.add_column('Username', justify='left', style='red')
        table.add_column('Password', justify='left', style='magenta')

        for row in matchedRows:
            table.add_row(row[0], row[2], row[3])
        console.print(table, end='\n')
    else:
        console.print(Text('No match found', style='red'))

    print('')    


# savepassword is compatible with this addrow
def AddRow():
    SavePassword()


# removes the row from password.enc
def RemoveRow():
    while True:
        console.print(Text('Enter the serial No: ', style='cyan'), end='')
        rowIndex = input()
        try:
            rowIndex = int(rowIndex) - 1
            if 0 <= rowIndex < len(tableClone):
                table = Table(header_style='bold', box=ROUNDED)
                table.add_column('Sr.no.', justify='left', style='yellow')
                table.add_column('Website', justify='left', style='red')
                table.add_column('Username', justify='left', style='magenta')
                table.add_column('Password', justify='left', style='red')
                table.add_row(tableClone[rowIndex][0], tableClone[rowIndex][1], tableClone[rowIndex][2], tableClone[rowIndex][3])

                console.print(table)

                mainMenu = [inquirer.List('menuChoice',
                                        message='Are you sure?',
                                        choices=['Yes', 'No'],
                            )]

                menuChoice = inquirer.prompt(mainMenu)
                userChoice = menuChoice['menuChoice']

                # main logic of password removing
                if userChoice == 'Yes':
                    with open('./data/password.enc', 'r') as file:
                        lines = file.readlines()
                    del lines[rowIndex]

                    with open('./data/password.enc', 'w') as file:
                        file.writelines(line for line in lines if line.strip())
                    file.close()

                    console.print(Text('Password removed successfully\n', style='yellow'))
                break
            else:
                console.print(Text('Invalid serial number', style='red'))
        except ValueError:
            console.print(Text('Please enter a valid number', style='red'))


# displays menu right below table
def getUpdates():
    menuChoicesList = [
        'Search a Password',
        'Add a Password',
        'Remove a Password',
        'Back'
    ]

    mainMenu = [inquirer.List('menuChoice',
                            message='Save the password?',
                            choices=menuChoicesList,
                )]

    menuChoice = inquirer.prompt(mainMenu)
    userChoice = menuChoice['menuChoice']
    
    if userChoice == 'Search a Password':
        SearchRow()
    elif userChoice == 'Add a Password':
        AddRow()
    elif userChoice == 'Remove a Password':
        RemoveRow()
    else:
        return False
    return True


# forms a rich table and decrypts the password
# TODO: color the table rows
def DisplayTable(key):
    table = Table(header_style='bold', box=ROUNDED)
    table.add_column('Sr.no.', justify='left', style='orange3')
    table.add_column('Website', justify='left', style='yellow')
    table.add_column('Username', justify='left', style='red')
    table.add_column('Password', justify='left', style='magenta')

    with open('./data/password.enc', 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start = 1):
            columns = line.strip().split('\t')

            if len(columns) == 3:
                website, username, password = columns
                decryptedPassword = DecryptPassword(password, key)
                table.add_row(str(i), website, username, decryptedPassword)
                columnClone = [str(i),website, username, decryptedPassword]
                tableClone.append(columnClone)
    file.close()
    console.print(table)
    print('')


# main function
def display():
    for _ in range(3):
        validKey, key = getMasterKey()
        if validKey:
            while True:
                DisplayTable(key)
                if not getUpdates():
                    break
            break    
    