l = list(range(10))

print(l[2:7])
print(l[::3])

l2 = list(l[:3])
l2.extend(l[-3:])
l2.reverse()

print(l2)