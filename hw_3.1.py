# HW 3.1. Найпростіший калькулятор

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a second number: "))
operator = input("Enter the arithmetic operator: ")

if operator == '*':
    result = number_1 * number_2
elif operator == '/':
    if number_2 == 0:
        result = "Division by zero"
    else:
        result = number_1 / number_2
elif operator == '+':
    result = number_1 + number_2
elif operator == '-':
    result = number_1 - number_2

print(result)