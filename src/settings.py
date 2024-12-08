import inquirer


def CustomizePassword():
    pass


def ChangeMasterKey():
    pass


def EraseData():
    pass


# main function
def settings():
    menuChoicesList = [
        'Customize Password',
        'Change the Master Key',
        'Erase All Data',
        'Back'
    ]

    mainMenu = [inquirer.List('menuChoice',
                             message='What would you like to do?',
                             choices=menuChoicesList,
                )]

    menuChoice = inquirer.prompt(mainMenu)
    userChoice = menuChoice['menuChoice']

    if userChoice == 'Customize Password':
        CustomizePassword()
    elif userChoice == 'Change the Master Key':
        ChangeMasterKey
    elif userChoice == 'Erase All Data':
        EraseData()
    else:
        pass
    