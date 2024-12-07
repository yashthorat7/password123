# co-main function
def SavePassword(password):
    website = input('Website: ')
    username = input('Username: ')
    
    encryptedPassword = password
    row = [website, username, encryptedPassword]

    with open('./data/password.enc', 'a') as file:
        rowText = str('website: ' + website+ ' username: '+ username+ ' password: '+ encryptedPassword+ '')
        file.write(rowText)

    print('Password saved successfully...\n')
    
