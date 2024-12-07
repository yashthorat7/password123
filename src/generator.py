import random
import string
from .encryption import SavePassword

def GeneratePassword(passwordLength):
    characters = string.ascii_letters + string.digits + string.punctuation
    Password = ''.join(random.choice(characters) for i in range(passwordLength))

    return Password


def DisplayPassword(Password):
    print(f'Generated Password: {Password}')


def AskSave(newPassword):
    # TODO: Ask yes no and again using inquier
    
    if True:
        SavePassword(newPassword)


def getPasswordLength():
    validLength = False

    while not validLength:
        MIN_LENGTH, MAX_LENGTH = 8, 64
        length = input('Enter the length of the password: ')
        if length == '':
            passwordLength = 8
            validLength = True
        else:
            try:
                passwordLength = int(length)
            except ValueError:
                print('Please enter a number or just leave it blank')
                continue
            
            if passwordLength < MIN_LENGTH:
                print(f'Password must be at least {MIN_LENGTH} characters long')
            elif passwordLength > MAX_LENGTH:
                print(f'Password must be at most {MAX_LENGTH} characters long')
            else:
                validLength = True

    return passwordLength


# main function
def generator():
    passwordLength = getPasswordLength()
    newPassword = GeneratePassword(passwordLength)
    DisplayPassword(newPassword)
    AskSave(newPassword)
    
