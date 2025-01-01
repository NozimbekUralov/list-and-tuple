t = (1, 2, 3) # elementlarni to'g'ridan to'gri o'zgartirib bo'lmaydi.

li = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)]

for i in li:
    print(li[li.index(i)])
