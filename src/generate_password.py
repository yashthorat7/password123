import random
from .file_handle import read_json

def select_nouns(words_data, combination):
    allNouns = words_data.get('small_nouns', []) + words_data.get('medium_nouns', []) + words_data.get('large_nouns', [])
    wordType = random.choice(combination)
    if wordType == 'nouns':
        return random.choice(allNouns)
    elif isinstance(wordType, str):
        return random.choice(words_data.get(wordType, []))
    return random.choice(wordType)

def select_words(length, combination, words_data):
    letter_password = []
    while sum(len(word) for word in letter_password) < length:
        nextWord = select_nouns(words_data, combination)
        if sum(len(word) for word in letter_password) + len(nextWord) <= length:
            letter_password.append(nextWord)
        else:
            break

    remaining_length = length - sum(len(word) for word in letter_password)
    if remaining_length > 0:
        letter_password.append(str(random.randint(10**(remaining_length - 1), 10**remaining_length - 1)))

    return ''.join(letter_password)

def alter_password(letter_password):
    passwordList = list(letter_password)
    length = len(passwordList)

    probabilities = {
        'toggleCase': 0.05 + (0.01 - 0.05) * (length - 8) / (64 - 8),
        'alterNum': 0.15 + (0.1 - 0.15) * (length - 8) / (64 - 8),
        'alterSymbol': 0.4 + (0.25 - 0.4) * (length - 8) / (64 - 8)
    }

    alters = read_json('alters.json');

    for i in range(length):
        char = passwordList[i]
        if random.random() < probabilities['toggleCase'] and char.islower():
            passwordList[i] = char.upper()
        elif char.lower() in alters and random.random() < probabilities['alterNum']:
            passwordList[i] = random.choice(alters[char.lower()]['number'])
        elif char in alters and random.random() < probabilities['alterSymbol']:
            passwordList[i] = random.choice(alters[char]['symbols'])

    Password = ''.join(passwordList)
    return Password

def generate_password(length):
    words_data = read_json('words.json')

    combinations_list = [
        ('nouns', 'nouns'),
        ('nouns', words_data['verbs']),
        (words_data['adjectives'], 'nouns'),
        (words_data['verbs'], 'nouns', 'nouns'),
        (words_data['adjectives'], 'nouns', words_data['verbs']),
        (words_data['verbs'], 'nouns', words_data['adjectives']),
        (words_data['verbs'], words_data['adjectives'], words_data['adverbs']),
        (words_data['adjectives'], 'nouns', 'nouns', words_data['verbs']),
        (words_data['verbs'], words_data['adjectives'], words_data['verbs'], 'nouns'),
        (words_data['verbs'], words_data['adjectives'], 'nouns', words_data['verbs'], words_data['adverbs']),
    ]

    combination = random.choice(combinations_list)
    letter_password = select_words(length, combination, words_data)
    password = alter_password(letter_password)
    return password