# concatenation
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

l4 = l1 + [7]  # [1, 2, 3, 7]
l1.extend([8, 9, 10])  # [1, 2, 3, 8, 9, 10]

# repetition
l5 = l1 * 2
print(l5)

# membership
l6 = [33, 44, 55, 88, 99]
print(44 in l6)

l7 = [[33, 44], 55, 88, 99]
print(44 in l7)
print([33, 44] in l7)

# list comparison
l8 = [1, 2, 3]
l9 = [1, 2, 3]
print(l1 == l6)
print(l8 == l9)
print(l1 < l6)
print(l8 > l6)
