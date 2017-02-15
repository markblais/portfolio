# A separate python file used to start the authentication process



import sys
import os
from time import sleep

# Clear the screen to simulate program is starting
os.system('clear')

# Variables for status bar
start_loading = '\n\n\n\nLoading'
loading = '.' * 159 + '\n\n'

# Used to simulate loading progress
print(start_loading)
for c in loading:
    print(c, end='')
    sys.stdout.flush()
    sleep(0.025)

# Start separate file for authentication
import authenticate
