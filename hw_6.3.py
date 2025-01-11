# HW 6.3. Добуток чисел

user_input = 999
# user_input = 1000
# user_input = 423
# user_input = 33
# user_input = 25
# user_input = 1

invalid_input_message = "Enter an integer"

if isinstance(user_input, int):
    digits_product = user_input
    while digits_product > 9:
        current_value = 1
        while digits_product > 0:
            current_value *= digits_product % 10
            digits_product = digits_product // 10
        digits_product = current_value
    print(digits_product)
else:
    print(invalid_input_message)
