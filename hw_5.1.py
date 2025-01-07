# HW 5.1. Ім'я змінної

import keyword
import string

user_input = input("Enter a variable name: ")

if user_input:
    if user_input == '_':
        result = True
    elif user_input[0].isdigit() or user_input in keyword.kwlist or '__' in user_input or not user_input.islower():
        result = False
    else:
        result = True
else:
    warning_message = "You didn't enter anything. Try again"

for i in user_input:
    if i in string.punctuation.replace('_', ' '):
        result = False

print(result if user_input else warning_message)