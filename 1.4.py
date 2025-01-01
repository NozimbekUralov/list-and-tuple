n1 = 1
n2 = 2
n3 = 3

if(n1 < n2):
    n3 += n1
    n1 = n3 -n1
    n3 -= n1

print(n1, n2, n3)