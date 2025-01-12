# HW 6.1. Діапазон букв

import string

# input_letters = "a-c".split('-')
# input_letters = "a-a".split('-')
# input_letters = "s-H".split('-')
# input_letters = "a-A".split('-')
input_letters = input("Введіть дві літери через дефіс (наприклад, a-z): ").split('-')


start_index = string.ascii_letters.find(input_letters[0])
end_index = string.ascii_letters.find(input_letters[-1])
result = string.ascii_letters[start_index:end_index + 1]

print(result)
