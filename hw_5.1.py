# HW 5.1. Ім'я змінної

import keyword
import string

user_input = '__name'
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

if user_input:

    if (user_input == '_' or
            (user_input.startswith('__') and len(user_input) > 2 and user_input[2].isalpha())):
        result = True

    elif (user_input[0].isdigit() or
          user_input in keyword.kwlist or
          '__' in user_input or
          not user_input.islower()):
        result = False

    else:
        result = True
else:
    result = False

for i in user_input:
    if i in string.punctuation.replace('_', ' '):
        result = False

print(result)
