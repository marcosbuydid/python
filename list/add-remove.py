l1 = [34, 44, 55, 78]

# add elements using append
l1.append(87)
l1.append('pascal')
l1.append([23, 41])
print(l1)

# add elements using extend
l1.extend([87, 65, 41])
print(l1)

l2 = [5, 47]
l2.extend('java')
print(l2)  # [5, 47, 'j', 'a', 'v', 'a']

l3 = [9, 7, 3]
l3.extend(range(7, 10))
print(l3)  # [9, 7, 3, 7, 8, 9]

# add elements using insert
l4 = [11, 22]
l4.insert(90, 'javascript')
print(l4)

l4[2:2] = [77]
print(l4)

l5 = l4.copy()
print(l5)

# remove elements using pop
l6 = [34, 54, 67, 89]
l6.pop()  # remove last element
print(l6)

l6.pop(1)  # using index
print(l6)

# remove elements using remove
l7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# if the element is not present on
# the list throw value error
l7.remove(9)
print(l7)

# remove elements using clear
l8 = [1, 2, 3]
# all occurrences of the list are removed
l8.clear()
print(l8)

# remove elements using del
del l7[0]
print(l7)

# specifying index range
del l7[0:2]
print(l7)
