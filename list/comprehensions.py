l = [x for x in range(1, 8)]
print(l)  # [1, 2, 3, 4, 5, 6, 7]

l1 = [x ** 2 for x in range(1, 8)]
print(l1)  # [1, 4, 9, 16, 25, 36, 49]

l2 = [x.lower() for x in 'vAcATIonS']
print(l2)  # ['v', 'a', 'c', 'a', 't', 'i', 'o', 'n', 's']

l3 = [int(x) for x in '12345']
print(l3)  # [1, 2, 3, 4, 5]

l4 = [x for x in 'abc*78ui_' if x.isalpha()]
print(l4)  # ['a', 'b', 'c', 'u', 'i']


