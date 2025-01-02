# HW 4.2. Знайти суму елементів із парними індексами
# =========================================

lst = [0, 1, 7, 2, 4, 8]
lst = [1, 3, 5]
lst = [6]
lst = []
num = 0
if not lst:
   print(0)
else:
   for i,v in enumerate(lst):
      if i % 2 == 0:
         num += v
   print(num * lst[-1])