# HW 8.3. Унікальне число

from collections import Counter


def find_unique_value(some_list):
    value_counts = Counter(some_list).most_common()[-1]
    unique_value = value_counts[0] if value_counts[1] == 1 else None
    return unique_value


assert find_unique_value([1, 2, 1, 1]) == 2, "Test1"
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, "Test2"
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, "Test3"
print("ОК")
