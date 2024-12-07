import rich


# called right after password generation
def SavePassword(password):
    website = input('Website: ')
    username = input('Username: ')
    
    encryptedPassword = password
    row = [website, username, encryptedPassword]

    with open('./data/password.enc', 'a') as file:
        rowText = str('website: ' + website+ ' username: '+ username+ ' password: '+ encryptedPassword+ '\n')
        file.write(rowText)

    print('\nPassword saved successfully...\n')
    
