L = [1, 2, 3, 4]
L1 = list((5, 6, 7, 8))
L2 = list('abcdef')
L3 = [1, 2, 3, 'abcdef', True, 5 + 6j]
print(L)
print(L1)
print(L2)
print(L3)

# add an element to a list
L1.append(34)
print(L1)

# modify an element from a list
L1[2] = 14
print(L1)

# remove an element from a list
L1.remove(8)
print(L1)
