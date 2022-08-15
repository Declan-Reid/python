#!/usr/bin/env python3
import random

# Set variables
password = ''
beginning = ''

# Get user input
while len(beginning) != 4:
    beginning = input("Enter the 4 characters to start the password below:\n")

password += beginning
length = int(input("Enter the length of the password below:\n"))

# Set strings of characters to use
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

# Add letters to password
for i in range(length-4):
    if i%2 == 0:
        password += letters[random.randint(0,25)]
    else:
        password += numbers[random.randint(0,9)]

# Check if password has numbers and letters
if not any(char.isdigit() for char in password):
    password = password.rstrip(1) + str(numbers[random.randint(0, 9)])

if not any(char.isalpha() for char in password):
    password = password.rstrip(1) + str(letters[random.randint(0, 25)])

print(password)