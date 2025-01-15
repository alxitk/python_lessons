# HW 7.3. Пошук підрядка


def second_index(text, some_str):
    if text.count(some_str) > 1:
        first_in_index = text.find(some_str) + 1
        result = text.find(some_str, first_in_index)
        return result


results = [
    second_index("sims", "s"),
    second_index("find the river", "e"),
    second_index("hi", "h"),
    second_index("hello, hello", "lo"),
]

print(results)
