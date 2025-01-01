# 1.
l = list(range(10))
print(l)

#2.
l.append(10)
del l[0]
print(l)

#3.
i = 0
while i < len(l):
    if(l[i] % 2) == 1:
        del l[i]
    else:
        i +=1

print(l)

#4.

from string import ascii_uppercase

l2 = list(ascii_uppercase)
lc = []

for i in l2:
    lc.append(i.lower())

print(lc)