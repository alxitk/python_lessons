# HW 8.1. Додати 1 до числа
def add_one(some_list):
    int_from_list = int("".join(str(i) for i in some_list))
    int_from_list += 1
    result = [int(i) for i in str(int_from_list)]
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")
