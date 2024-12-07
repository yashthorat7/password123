def DisplayTitle():
    print(r''' ____   _    ____ ______        _____  ____  ____  _ ____  _____ 
|  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \/ |___ \|___ / 
| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | | | __) | |_ \ 
|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| | |/ __/ ___) |
|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/|_|_____|____/ 
''')

def main():
    print('1. Generate a Password')
    print('2. Saved Passwords')
    print('3. Settings')
    print('4. Exit')
    choice = input('Enter a choice: ')

    if choice == '1':
        print('Generate a Password')
    elif choice == '2':
        print('Saved Passwords')
    elif choice == '3':
        print('Settings')
    elif choice == '4':
        print('Exit')
    else:
        print('Invalid choice')

if __name__ == '__main__':
    DisplayTitle()
    while True:
        main()