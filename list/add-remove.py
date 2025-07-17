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
