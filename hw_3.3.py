# HW 3.3. Розділити один список на два списки


lst = []
# lst = [1]
# lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = [1, 2, 3, 4, 5]
new_lst = []

if not lst:
    new_lst = [[], []]
elif len(lst) % 2 == 0:
    new_lst.append(lst[:int(len(lst) / 2)])
    new_lst.append(lst[int(len(lst) / 2):])
else:
    new_lst.append(lst[:(len(lst) // 2) + 1])
    new_lst.append(lst[(len(lst) // 2) + 1:])

print(new_lst)




