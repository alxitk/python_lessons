# ДЗ 2.2. Необхідно "перевернути" 5-ти значне число

user_input_number = int(input("Enter a five-digit number: "))
print(user_input_number % 10)
user_input_number = user_input_number//10
print(user_input_number % 10)
user_input_number //= 10
print(user_input_number % 10)
user_input_number //= 10
print(user_input_number % 10)
user_input_number //= 10
print(user_input_number % 10)
