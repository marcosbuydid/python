l = [10, 20, 30, 40, 10, 20, 30, 40]
# index of the first occurrence of the
# element on the list
l.index(20)  # 1
print(l.index(20, 2))
print(l.index(20, 2, 6))

# occurrences of an element on a list
print(l.count(10))  # 2

# reverse an entire list
l.reverse()
print(l)

l1 = [30, 70, 50, 10, 20, 1, 5]
# sort elements of a list on increase order
l1.sort()
print(l1)

l2 = [90, 70, 10, 1, 25, 7, 9]
# sort elements of a list on decrease order
l2.sort(reverse=True)
print(l2)

l3 = ['cat', 'vacations', 'couple', 'summer']
# sort elements of a list alphabetically
l3.sort()
print(l3)

l4 = ['cat', 'dog', 'sea', 'vacations', 'couple', 'summer']
# sort elements of a list based on elements length
l4.sort(key=len)
print(l4)

# sort elements of a list ignoring if elements are
# lowercase or uppercase
l5 = ['Winter', 'Fog', 'books']
l5.sort(key=str.lower)
print(l5)
