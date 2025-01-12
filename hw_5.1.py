# HW 5.1. Ім'я змінної

import keyword
import string

# user_input = '__name'
# user_input = '__double__twice'
# user_input = 'within__name'
# user_input = '_'
# user_input = '__'
# user_input = '___'
# user_input = 'x'
# user_input = 'get_value'
# user_input = 'get value'
# user_input = 'get!value'
# user_input = 'some_super_puper_value'
# user_input = 'Get_value'
# user_input = 'get_Value'
# user_input = 'getValue'
# user_input = '3m'
# user_input = 'm3'
# user_input ='assert'
# user_input = 'assert_exception'

result = True
user_input = input('Enter a variable name: ')

if user_input:
    for i in user_input:
        if i in string.punctuation.replace('_', ' '):
            result = False

    if (user_input[0].isdigit() or
            not user_input.islower() or
            user_input in keyword.kwlist):
        result = False

    if (user_input.startswith('__') and
            user_input.count('__') > 1 or
            '__' in user_input[2:]):
        result = False

    if user_input == '_':
        result = True
else:
    result = False

print(result)
