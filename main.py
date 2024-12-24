# print("Hello World")


# # ДЗ 2.1. Виведення числа в стовпчик

user_input_number = int(input("Enter a four-digit number: "))
print(user_input_number//1000)
user_input_number = user_input_number % 1000
print(user_input_number//100)
user_input_number = user_input_number % 100
print(user_input_number//10)
print(user_input_number % 10)