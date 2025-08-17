list1 = [100, -2, 3, 56, 67, 2]
print(sorted(list1))
print(sorted(list1, reverse=True))
print(sorted(list1, key=abs))

# reverse a sequence
rev = reversed(list1)
print(list(rev))

list2 = [140, -21, 13, 54, 67, 22]
s = slice(3)
print(list2[s])

list3 = [15, 21, 13, 4, 5]
it = iter(list3)
print(next(it))
