# Authentication File


import os
import getpass


# Clear the screen to simulate program is starting
os.system('clear')

# Welcome
print('\n' * 10 + ' ' * 62 + ' Welcome to A Heart Filled With Love')

# User Authentication

firstName = input('\n\n\n\n' + ' ' * 66 + "Please enter your first name:\n\n" + ' ' * 78)

if (firstName == 'Gina'):
    lastName = input('\n\n' + ' ' * 66 + "Please enter your last name:\n\n" + ' ' * 77)
    if (lastName == 'Mouchet'):
        # getpass used to keep password characters private while typing
        pin = getpass.getpass('\n\n' + ' ' * 69 + "Please enter your PIN:\n\n" + ' ' * 78)
        if (pin == '1351'):
            # Start separate file for main program
            import valentine
        else:
            print('\n' * 4 + ' ' * 73 + 'Access Denided!')
            print('\n\n' + ' ' * 68 + 'A Heart Filled With Love')
            print('\n\n' + ' ' * 73 + 'Copyright 2017')
            print('\n' * 4)
    else:
        print('\n' * 4 + ' ' * 73 + 'Access Denided!')
        print('\n\n' + ' ' * 68 + 'A Heart Filled With Love')
        print('\n\n' + ' ' * 73 + 'Copyright 2017')
        print('\n' * 4)
else:
    print('\n' * 4 + ' ' * 73 + 'Access Denided!')
    print('\n\n' + ' ' * 68 + 'A Heart Filled With Love')
    print('\n\n' + ' ' * 73 + 'Copyright 2017')
    print('\n' * 4)
