# HW 4.1. Перемістити всі нулі до кінця списку

lst = [0]
lst = [0, 1, 0, 12, 3]
lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
counter = 0
if 0 in lst:
    while 0 in lst:
        lst.remove(0)
        counter += 1

lst.extend([0] * counter)
print(lst)
