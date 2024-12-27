import random
import inquirer
import json
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.box import ROUNDED
from .encryption import SavePassword

console = Console()


def ValidatePassword(password):
    '''checks if the password is valid'''
    passwordLength = len(password)

    minLowLetters = int(2 + (19 - 2) * (passwordLength - 8) / (64 - 8))
    minUpLetters = int(1 + (6 - 1) * (passwordLength - 8) / (64 - 8))
    minNumbers = int(1 + (8 - 1) * (passwordLength - 8) / (64 - 8))
    minSymbols = int(2 + (10 - 2) * (passwordLength - 8) / (64 - 8))

    lowLettersCount = sum(1 for char in password if char.islower())
    upLetterCount = sum(1 for char in password if char.isupper())
    numbersCount = sum(1 for char in password if char.isdigit())
    symbolsCount = sum(1 for char in password if char in '!@#$%^&*()_+=-?')

    return (
        lowLettersCount >= minLowLetters
        and upLetterCount >= minUpLetters
        and numbersCount >= minNumbers
        and symbolsCount >= minSymbols
    )


def AlterPassword(password):
    '''alters the letters of the generated password'''
    passwordList = list(password)
    passwordLength = len(passwordList)

    probabilities = {
        "toggleCase": 0.05 + (0.01 - 0.05) * (passwordLength - 8) / (64 - 8),
        "alterNum": 0.15 + (0.1 - 0.15) * (passwordLength - 8) / (64 - 8),
        "alterSymbol": 0.4 + (0.25 - 0.4) * (passwordLength - 8) / (64 - 8)
    }

    with open('data/alters.json', 'r') as file:
        alters = json.load(file)

    for i in range(passwordLength):
        char = passwordList[i]
        if random.random() < probabilities["toggleCase"] and char.islower():
            passwordList[i] = char.upper()
        elif char.lower() in alters and random.random() < probabilities["alterNum"]:
            passwordList[i] = random.choice(alters[char.lower()]['number'])
        elif char in alters and random.random() < probabilities["alterSymbol"]:
            passwordList[i] = random.choice(alters[char]['symbols'])

    newPassword = ''.join(passwordList)
    return newPassword if ValidatePassword(newPassword) else None


def GenerateWord(wordsData, combination):
    '''fetches the data from words.json'''
    all_nouns = wordsData.get('small_nouns', []) + wordsData.get('medium_nouns', []) + wordsData.get('large_nouns', [])
    wordType = random.choice(combination)
    if wordType == 'nouns':
        return random.choice(all_nouns)
    elif isinstance(wordType, str):
        return random.choice(wordsData.get(wordType, []))
    return random.choice(wordType)


def BuildPassword(passwordLength, combination, wordsData):
    '''appends the words or number into the password'''
    password = []
    while sum(len(word) for word in password) < passwordLength:
        nextWord = GenerateWord(wordsData, combination)
        if sum(len(word) for word in password) + len(nextWord) <= passwordLength:
            password.append(nextWord)
        else:
            break

    remainingLength = passwordLength - sum(len(word) for word in password)
    if remainingLength > 0:
        password.append(str(random.randint(10**(remainingLength - 1), 10**remainingLength - 1)))

    return password


def GeneratePassword(passwordLength):
    '''password generation logic'''
    with open('data/words.json', 'r') as file:
        wordsData = json.load(file)

    combinations = [
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

    combination = random.choice(combinations)
    password = BuildPassword(passwordLength, combination, wordsData)
    newPassword = AlterPassword(''.join(password))
    while not newPassword:
        password = BuildPassword(passwordLength, combination, wordsData)
        newPassword = AlterPassword(''.join(password))
    return newPassword


def DisplayPassword(password):
    '''displays the generated password in rich panel'''
    passwordText = Text('Generated Password: ', style='green') + Text(password, style='yellow')
    passwordContainer = Panel(passwordText, style='bold', expand=False, box=ROUNDED)
    console.print(passwordContainer)


def GetSave(password):
    '''asks if user wants to save the generated password or not'''
    print('')
    menuChoicesList = ['Yes', 'No', 'Generate Again']
    menuChoice = inquirer.prompt([inquirer.List('menuChoice', message='Save the password?', choices=menuChoicesList)])['menuChoice']

    if menuChoice == 'Yes':
        SavePassword(os.getenv('MASTER_KEY'), password)
    elif menuChoice == 'Generate Again':
        generator(1)


def GetPasswordLength(take):
    '''asks the password length'''
    while True:
        with open('./data/settings.json', 'r') as file:
            settings = json.load(file)

        if settings['defaultForce'] and take == 0:
            passwordLength = settings['defaultForceNum']
            return passwordLength

        defaultLength = settings['default']
        console.print(
            Text('Enter the length of the password ', style='purple') +
            Text(f'(default={defaultLength})', style='blue') +
            Text(': ', style='purple'),
            end=''
        )
        lengthInput = input()

        if not lengthInput:
            return defaultLength
        try:
            passwordLength = int(lengthInput)
            if 8 <= passwordLength <= 64:
                return passwordLength
            console.print(Text('Password length must be between 8 and 64 characters.', style='red'))
        except ValueError:
            console.print(Text('Please enter a valid number.', style='red'))


# main function
def generator(take = 0):
    passwordLength = GetPasswordLength(take)
    newPassword = GeneratePassword(passwordLength)
    DisplayPassword(newPassword)
    GetSave(newPassword)
