s = [True, 1, 1.1, "text", "text", "text", "text"]
s2 = []

for i in s:
    if(type(i) == str):
        i = i.upper()
        s2.append(i)

print(s2)