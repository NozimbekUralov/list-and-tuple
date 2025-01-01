l = []
l1 = []

l.append(list(range(4)))
l.append(list(range(4)))
l.append(list(range(4)))

for i in l:
    l1.append(i[-1])

t = tuple(l1)

print(t)