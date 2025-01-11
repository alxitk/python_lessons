# HW 6.2. Конвертер із числа в дату

user_input = 0
# user_input = 224930
# user_input = 466289
# user_input = 950400
# user_input = 1209600
# user_input = 1900800
# user_input = 8639999
# user_input = 22493
# user_input = 7948799

VALID_RANGE = range(0, 8640000)
user_input_copy = user_input
invalid_input_message = "Enter a number from the range 0 to 8640000"

DAYS_WORD_FORM = ('днів', 'дні', 'день')
SECONDS_IN_TIME_UNITS = {
    'seconds_in_day': 86400,
    'seconds_in_hour': 3600,
    'seconds_in_minute': 60
}

unformatted_time = []

for i in SECONDS_IN_TIME_UNITS.values():
    unformatted_time.append(str(user_input_copy // i).zfill(2))
    user_input_copy %= i
unformatted_time.append(str(user_input_copy).zfill(2))

days = int(unformatted_time.pop(0))

if ((days // 10) % 10 == 1) and (days % 10 in [1, 2, 3, 4]):
    day_word_form = DAYS_WORD_FORM[0]

elif 2 <= days % 10 <= 4:
    day_word_form = DAYS_WORD_FORM[1]

elif days % 10 == 1:
    day_word_form = DAYS_WORD_FORM[2]

else:
    day_word_form = DAYS_WORD_FORM[0]

result = f"{days} {day_word_form}, {':'.join(unformatted_time)}"

print(result if user_input in VALID_RANGE else invalid_input_message)
