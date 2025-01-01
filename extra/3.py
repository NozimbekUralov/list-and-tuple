# create a list of 10 fruits
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "pear", "peach", "plum"]
rev_fruits = []
count = 1

for fruit in fruits:
    if count == 3:
        rev_fruits.append(fruit[::-1])
        count = 1
    else:
        rev_fruits.append(fruit)
        count += 1


t= tuple(rev_fruits)

print(t.index("pear"))