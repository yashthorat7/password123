import random
import string
from ..file_handle import read_json

def read_structure(word):
    digits = sum(1 for char in word if char.isdigit())
    capital_letters = sum(1 for char in word if char.isupper())
    symbols = sum(1 for char in word if char in string.punctuation)
    small_letters = sum(1 for char in word if char.islower())
    return [digits, capital_letters, symbols, small_letters]

def select_words(min_length, length, combination):
    words_data = read_json('words.json')
    attempt_limit = 20
    for _ in range(attempt_limit):
        letter_password = []
        current_length = 0
        attempts = 0
        while current_length < min_length - 1:
            attempts += 1
            if attempts > 20:
                combination = list(combination) + ['nouns']
            letter_password = []
            current_length = 0
            for word_type in combination:
                if word_type in words_data:
                    next_word = random.choice(words_data[word_type])
                    letter_password.append(next_word)
                    current_length += len(next_word)
                    if current_length >= length - 1:
                        break

            if min_length - 2 <= current_length <= length - 2:
                return ''.join(letter_password)

def case_change(length, letter_password):
    password_list = list(letter_password)
    for i in range(1, length):
        if password_list[i].islower() and random.random() < 0.5:
            password_list[i] = password_list[i].upper()
    password_list[0] = password_list[0].upper()
    return ''.join(password_list)

def alter_password(length, cased_password):
    alters = read_json('alters.json')
    password_list = list(cased_password)
    altered_count = 0
    
    while altered_count < length:
        i = random.randint(0, len(password_list) - 1)
        char = password_list[i]
        
        if char.islower() and char in alters:
            altered_char = random.choice(alters[char]['symbols'])
            password_list[i] = altered_char
            altered_count += 1
    return ''.join(password_list)

def get_combination(length, combinations_list):
    scaling_factor = max((length - 8) / (64 - 8), 0)
    max_index = len(combinations_list) - 1
    index = int(scaling_factor * max_index)
    return random.choice(combinations_list[:index + 1])

def add_remaining_digits(length, letter_password):

    remaining_length = length - len(letter_password)
    if remaining_length > 0:
        return letter_password + str(random.randint(10**(remaining_length - 1), 10**remaining_length - 1))
    return letter_password

def generate_password(length, structure):
    combinations_list = [
        ('nouns', 'nouns'),
        ('nouns', 'verbs'),
        ('adjectives', 'nouns'),
        ('verbs', 'nouns', 'nouns'),
        ('adjectives', 'nouns', 'verbs'),
        ('verbs', 'nouns', 'adjectives'),
        ('verbs', 'adjectives', 'adverbs'),
        ('adjectives', 'nouns', 'nouns', 'verbs'),
        ('verbs', 'adjectives', 'verbs', 'nouns'),
        ('verbs', 'adjectives', 'nouns', 'verbs', 'adverbs'),
    ]

    min_length = structure[1] + structure[2] + structure[3]
    combination = get_combination(length, combinations_list)
    # print('combination:', combination)
    letter_password = select_words(min_length, length, combination)
    # print('letter_password:', letter_password)
    numbered_password = add_remaining_digits(length, letter_password)
    # print('numbered_password:', numbered_password)
    cased_password = case_change(structure[1], numbered_password)
    # print('cased_password:', cased_password)
    password = alter_password(structure[2], cased_password)
    # print('password:', password)
    # print('structure:', structure)
    # print('see structure:', read_structure(password))
    return password