import random
import string
import inquirer
import json
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.box import ROUNDED
from .encryption import SavePassword

console = Console()

def getNoun(nounsData):
    nounType = random.choice(['small_nouns', 'medium_nouns', 'large_nouns'])
    randomNoun = random.choice(nounsData[nounType])
    return randomNoun

def checkPasswordFill(passwordLength, password):
    with open('data/words.json', 'r') as file:
        wordsData = json.load(file)
    
    currentLength = sum(len(word) for word in wordsData)
    remainingSpace = passwordLength - currentLength
    
    if remainingSpace > 0:
        if remainingSpace <= 3:
            password.append(str(random.randint(10**(remainingSpace-1), 10**remainingSpace - 1)))
        else:
            password.append(random.choice(wordsData['verbs'] + wordsData['adjectives'] + wordsData['adverbs']))
    elif remainingSpace < 0:
        password.pop()
        if abs(remainingSpace) >= 4:
            password.append(random.choice(wordsData['verbs'] + wordsData['adjectives'] + wordsData['adverbs']))
        else:
            password.append(str(random.randint(10**(abs(remainingSpace)-1), 10**abs(remainingSpace) - 1)))
    
    return password

# generates a password
def GeneratePassword(passwordLength):
    with open('data/words.json', 'r') as file:
        wordsData = json.load(file)

    possibleCombinations = [
        ('nouns', wordsData['verbs']),
        (wordsData['adjectives'], 'nouns'),
        (wordsData['verbs'], wordsData['adjectives'], wordsData['adverbs']),
        (wordsData['adjectives'], 'nouns', wordsData['verbs']),
        (wordsData['verbs'], 'nouns', 'nouns'),
        (wordsData['adjectives'], 'nouns', 'nouns', wordsData['verbs']),
        (wordsData['verbs'], 'nouns', 'nouns'),
        (wordsData['verbs'], 'nouns', wordsData['adjectives']),
        (wordsData['verbs'], wordsData['adjectives'], 'nouns', wordsData['verbs'], wordsData['adverbs']),
        (wordsData['verbs'], wordsData['adjectives'], wordsData['verbs'], 'nouns'),
        ('nouns', 'nouns')
    ]

    passwordParts = []

    while sum(len(word) for word in passwordParts) < passwordLength:
        combination = random.choice(possibleCombinations)
        tempParts = []

        for part in combination:
            if part == 'nouns':
                selectedNoun = getNoun(wordsData)
                tempParts.append(selectedNoun)
            else:
                selectedWord = random.choice(part)
                tempParts.append(selectedWord)
        passwordParts.extend(tempParts)

    adjustedPassword = checkPasswordFill(passwordLength, passwordParts)
    
    return ''.join(str(word) for word in adjustedPassword)


# used rich panel to show password in a box
def DisplayPassword(password):
    passwordText = Text('Generated Password: ', style='green') + Text(password, style='yellow')

    passwordContainer = Panel(passwordText, style='bold', expand=False, box=ROUNDED)
    console.print(passwordContainer)
    print('')


#jumps to the encryption.py if true
def getSave(password):
    menuChoicesList = [
        'Yes',
        'No',
        'Generate Again'
    ]

    mainMenu = [inquirer.List('menuChoice',
                            message='Save the password?',
                            choices=menuChoicesList,
                )]

    menuChoice = inquirer.prompt(mainMenu)
    userChoice = menuChoice['menuChoice']
    
    if userChoice == 'Yes':
        env = os.getenv('MASTER_KEY')
        SavePassword(env, password)
    elif userChoice == 'No':
        return
    else:
        generator(1)


# gets the length of the password and validates it
def getPasswordLength(i):
    validLength = False

    while not validLength:
        MIN_LENGTH, MAX_LENGTH = 8, 64

        with open ('./data/settings.json', 'r') as file:
            data = json.load(file)

        defaultForce = data['defaultForce']
        file.close()

        if defaultForce:
            DEFAULT_LENGTH = data['defaultForceNum']
        else:
            DEFAULT_LENGTH = data['default']

        length = ''
        if not defaultForce or i == 1:
            console.print(Text('Enter the length of the password ', style='purple') + Text(f'(default={DEFAULT_LENGTH})', style='blue') + Text(': ', style='purple'), end='')
            length = input()

        if length == '':
            passwordLength = DEFAULT_LENGTH
            validLength = True
        else:
            try:
                passwordLength = int(length)
            except ValueError:
                console.print('Please enter a valid number', style='red')
                continue
            
            if passwordLength < MIN_LENGTH:
                console.print(Text(f'Password must be at least {MIN_LENGTH} characters long', style='red'))
            elif passwordLength > MAX_LENGTH:
                console.print(Text(f'Password must be at most {MAX_LENGTH} characters long', style='red'))
            else:
                validLength = True

    return passwordLength


# main function
def generator(i = 0):
    passwordLength = getPasswordLength(i)
    newPassword = GeneratePassword(passwordLength)
    DisplayPassword(newPassword)
    getSave(newPassword)
    