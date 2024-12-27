# HW 3.2. Перемістити елемент у списку

lst = []
# lst = [1]
# lst =  [12, 3, 4, 10]
# lst =  [12, 3, 4, 10, 8]
if len(lst) <= 1:
    print(lst)
else:
    new_lst = lst.pop()
    lst.insert(0, new_lst)
    print(lst)