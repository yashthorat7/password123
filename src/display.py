import os
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED
from .encryption import DecryptPassword

console = Console()
load_dotenv()

# checks if the master key is correct
def getMasterKey():
    console.print(Text('Enter the Master Key: '), style='cyan', end='')
    key = input()
    
    if (key == ''):
        console.print(Text('Master Key cannot be empty!', style='red'), end='\n')
    elif (key != os.getenv('MASTER_KEY')):
        console.print(Text('Invalid Master Key!', style='red'), end='\n')

    return key == os.getenv('MASTER_KEY'), key

# forms a rich table and decrypts the password
# TODO: color the table rows
def DisplayTable(key):
    table = Table(header_style='bold', box=ROUNDED)
    table.add_column('Website', justify='left', style='yellow')
    table.add_column('Username', justify='left', style='red')
    table.add_column('Password', justify='left', style='magenta')

    with open('./data/password.enc', 'r') as file:
        for line in file.readlines():
            columns = line.strip().split('\t\t')
            if len(columns) == 3:
                website, username, password = columns
                decryptedPassword = DecryptPassword(password, key)
                table.add_row(website, username, decryptedPassword)
    file.close()
    console.print(table, end='\n')

# main function
def display():
    validKey, key = getMasterKey()
    
    if validKey:
        DisplayTable(key)
    else:
        display()
