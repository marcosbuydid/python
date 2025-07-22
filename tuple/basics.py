t = (1, 2, 3, 4, 5, 6)
t1 = (1.4, 1.4, 2.8, 3.5)
t2 = ('Clari', 'John', 'Dave')
t3 = (9, 3.4, 'Clari', True, 5 + 6j)
print(t)
print(t1)
print(t2)
print(t3)

t4 = ([1, 2, 3, 4, 5, 6])
t5 = tuple([1, 2, 3])
t6 = tuple('pandas')
t7 = tuple(range(1, 9))
print(t5)

for x in t7:
    print(x, end=" ")
