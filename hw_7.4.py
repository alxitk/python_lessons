# HW 7.4. Пошук спільних елементів


def common_elements():
    multiples_of_3 = {i for i in range(100) if i % 3 == 0}
    multiples_of_5 = {i for i in range(100) if i % 5 == 0}
    intersection = set.intersection(multiples_of_3, multiples_of_5)
    return intersection


print(common_elements())
