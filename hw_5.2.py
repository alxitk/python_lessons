user_input = 'y'
while user_input == 'y':
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
    print(result if (number_2 == 0 and operator == '/') else f"{number_1} {operator} {number_2} = {result}")
    user_input = input('Start calculate again?: y/n ').lower()






