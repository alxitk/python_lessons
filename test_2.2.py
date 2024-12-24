# # ДЗ 2.2. Необхідно "перевернути" 5-ти значне число

reverse_user_input_number = 0
user_input_number = int(input("Enter a five-digit number: "))

reverse_user_input_number = user_input_number % 10 * 10000
user_input_number = user_input_number//10
reverse_user_input_number += (user_input_number % 10) * 1000
user_input_number //= 10
reverse_user_input_number += (user_input_number % 10) * 100
user_input_number //= 10
reverse_user_input_number += (user_input_number % 10) * 10
user_input_number //= 10
reverse_user_input_number += (user_input_number % 10) * 1

print(reverse_user_input_number)