s = "Hello World!"
s2 = ""
s3 = "Python programming is amazing!"
l2 = []
l = []

for i in s:
    l.append(i)

print(l)

s2 = "".join(l)

print(s2)

l2 = s3.split(" ")
print(l2, end="\n")

s2 = ""
for i in l2:
    s2 += "".join(i[0])

print(s2)
