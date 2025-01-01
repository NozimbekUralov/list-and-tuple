t = tuple(range(5))

for i in t:
    print(i, t.count(i))

print("by index: ", t[t.index(3)])

t1 = (1,2,3,4,5,6,7,3,43,3)

m = 1

for i in t1:
    temp = t1.count(i)
    if(temp > m):
        m = temp
        mi = t1.index(i)

print(t1[mi], ":", m, "times")