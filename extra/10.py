l = [1, 2, 32, 23, 3, 5, 'text', 'text2', 'text3', 'text4', 'text5']
ln = []

for n in l:
    if type(n) == int:
        ln.append(n)

ln.sort()

print(ln)
