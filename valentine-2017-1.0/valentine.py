# Title: A Heart Filled With Love


# Modules ###########################################################################################

# Module used to display the date and time during the program.
import time
import sys
import os
from time import sleep


# Variables #########################################################################################

# Variables for status bar
start_loading = '\n\n\n\nLoading'
loading = '.' * 159 + '\n\n'

# Variables containing letter "x" and "o" used individually.
item_one = 'x'
item_two = 'o'

# Variable combo of letter "x" and "o"
items = item_one + \
        item_two

# Variable used to reverse the order of "xo" to "ox".
reversed_items = item_two + \
        item_one


# Authentication ####################################################################################

# Used to enter the string "clear" into the Command Line Interface and clear the screen
os.system('clear')

# Authentication has passed
print('\n' * 10 + ' ' * 75 + 'Access Granted!')
print('\n' + ' ' * 74 + 'Hello Gina xox  ;)')

# Used to simulate loading progress of the main program
print(start_loading)
for c in loading:
    print(c, end='')
    sys.stdout.flush()
    sleep(0.025)

# Clear the screen to simulate program is starting
os.system('clear')


# The Design Code ###################################################################################

# Prints the top border.
print(items * 79 + item_one + '\n' + items + ' ' * 155 + reversed_items)

# Displays date and time.
localtime = time.asctime( time.localtime(time.time()) )
print(items + ' ' * 66 + localtime + ' ' * 65 + reversed_items)

# The Greeting
print(items + ' ' * 67 + 'Happy Valentine\'s Day !' + ' ' * 65 + reversed_items)


# Heart Section 1 of 3: Pattern -2 +2 -4 +2 -2

# Line 1
print(items + ' ' * 36 + items * 13 + 'x' + ' ' * 31 + items * 13 + 'x' + ' ' * 34 + reversed_items)
# Line 2
print(items + ' ' * 34 + items * 15 + 'x' + ' ' * 27 + items * 15 + 'x' + ' ' * 32 + reversed_items)
# Line 3
print(items + ' ' * 32 + items * 17 + 'x' + ' ' * 23 + items * 17 + 'x' + ' ' * 30 + reversed_items)
# Line 4
print(items + ' ' * 30 + items * 19 + 'x' + ' ' * 19 + items * 19 + 'x' + ' ' * 28 + reversed_items)
# Line 5
print(items + ' ' * 28 + items * 21 + 'x' + ' ' * 15 + items * 21 + 'x' + ' ' * 26 + reversed_items)
# Line 6
print(items + ' ' * 26 + items * 23 + 'x' + ' ' * 11 + items * 23 + 'x' + ' ' * 24 + reversed_items)
# Line 7
print(items + ' ' * 24 + items * 25 + 'x' + ' ' * 7 + items * 25 + 'x' + ' ' * 22 + reversed_items)
# Line 8
print(items + ' ' * 22 + items * 27 + 'x' + ' ' * 3 + items * 27 + 'x' + ' ' * 20 + reversed_items)


# Heart Section 2 of 3: No number pattern
# The maximum span of the Heart with a message in the middle.

# Line 9
print(items + ' ' * 22 + items * 27 + 'x' + ' G ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 10
print(items + ' ' * 22 + items * 27 + 'x' + ' i ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 11
print(items + ' ' * 22 + items * 27 + 'x' + ' n ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 12
print(items + ' ' * 22 + items * 27 + 'x' + ' a ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 13
print(items + ' ' * 22 + items * 27 + 'x' + '   ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 14
print(items + ' ' * 22 + items * 27 + 'x' + ' & ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 15
print(items + ' ' * 22 + items * 27 + 'x' + '   ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 16
print(items + ' ' * 22 + items * 27 + 'x' + ' M ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 17
print(items + ' ' * 22 + items * 27 + 'x' + ' a ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 18
print(items + ' ' * 22 + items * 27 + 'x' + ' r ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 20
print(items + ' ' * 22 + items * 27 + 'x' + ' k ' + items * 27 + 'x' + ' ' * 20 + reversed_items)
# Line 21
print(items + ' ' * 22 + items * 27 + 'x' + ' ' * 3 + items * 27 + 'x' + ' ' * 20 + reversed_items)


# Heart Section 3 of 3: Pattern +2 -2 +2
# The Heart tapers off

# Line 22
print(items + ' ' * 24 + items * 54 + item_one + ' ' * 22 + reversed_items)
# Line 23
print(items + ' ' * 26 + items * 52 + item_one + ' ' * 24 + reversed_items)
# Line 24
print(items + ' ' * 28 + items * 50 + item_one + ' ' * 26 + reversed_items)
# Line 25
print(items + ' ' * 30 + items * 48 + item_one + ' ' * 28 + reversed_items)
# Line 26
print(items + ' ' * 32 + items * 46 + item_one + ' ' * 30 + reversed_items)
# Line 27
print(items + ' ' * 34 + items * 44 + item_one + ' ' * 32 + reversed_items)
# Line 28
print(items + ' ' * 36 + items * 42 + item_one + ' ' * 34 + reversed_items)
# Line 29
print(items + ' ' * 38 + items * 40 + item_one + ' ' * 36 + reversed_items)
# Line 30
print(items + ' ' * 40 + items * 38 + item_one + ' ' * 38 + reversed_items)
# Line 31
print(items + ' ' * 42 + items * 36 + item_one + ' ' * 40 + reversed_items)
# Line 32
print(items + ' ' * 44 + items * 34 + item_one + ' ' * 42 + reversed_items)
# Line 33
print(items + ' ' * 46 + items * 32 + item_one + ' ' * 44 + reversed_items)
# Line 34
print(items + ' ' * 48 + items * 30 + item_one + ' ' * 46 + reversed_items)
# Line 35
print(items + ' ' * 50 + items * 28 + item_one + ' ' * 48 + reversed_items)
# Line 36
print(items + ' ' * 52 + items * 26 + item_one + ' ' * 50 + reversed_items)
# Line 37
print(items + ' ' * 54 + items * 24 + item_one + ' ' * 52 + reversed_items)
# Line 38
print(items + ' ' * 56 + items * 22 + item_one + ' ' * 54 + reversed_items)
# Line 39
print(items + ' ' * 58 + items * 20 + item_one + ' ' * 56 + reversed_items)
# Line 40
print(items + ' ' * 60 + items * 18 + item_one + ' ' * 58 + reversed_items)
# Line 41
print(items + ' ' * 62 + items * 16 + item_one + ' ' * 60 + reversed_items)

# Heart is finished, but the left and right borders continue building "xo" and "ox"
print(items + ' ' * 155 + reversed_items)

# Prints the bottom border.
print(items * 79 + item_one)

# Prints spaces to add padding between bottom border and command prompt
#print('\n' * 10)
