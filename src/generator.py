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


def generateNextWord(wordsData, combination):
    wordType = random.choice(combination)
    if wordType == 'nouns':
        return getNoun(wordsData)
    elif isinstance(wordType, str):
        return random.choice(wordsData[wordType])
    else:
        return random.choice(wordType)


def checkPassword(passwordLength, password, wordsData, currentCombination):
    currentLength = sum(len(word) for word in password)
    
    if currentLength == passwordLength:
        return password

    if currentLength < passwordLength:
        remainingLength = passwordLength - currentLength
        if remainingLength <= 3:
            random_number = str(random.randint(10**(remainingLength - 1), 10**remainingLength - 1))
            password.append(random_number)
        else:
            nextWord = generateNextWord(wordsData, currentCombination)
            password.append(nextWord)
        return checkPassword(passwordLength, password, wordsData, currentCombination)

    elif currentLength > passwordLength:
        password.pop()
        nextWord = generateNextWord(wordsData, currentCombination)
        password.append(nextWord)
        return checkPassword(passwordLength, password, wordsData, currentCombination)


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

    currentCombination = random.choice(possibleCombinations)
    password = []
    password = checkPassword(passwordLength, password, wordsData, currentCombination)

    return ''.join(password)



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
    
