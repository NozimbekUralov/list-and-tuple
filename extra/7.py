s = "Python and data structures are interesting!"
ls = []
l = []

for i in s:
    ls.append(i)

print(ls)

for i in s:
    if i.islower():
        l.append(i)

print(l)
