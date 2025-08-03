S = {23, 45, 65, 78, 96}
S1 = {10, 100, 500}

# add
S.add(101)
S.add((102, 103))
print(S)

# update
S.update((201, 202))
print(S)

S1.update('swift')
print(S1)

# copy
S2 = S.copy()
print(S2)

# pop (remove last element)
S3 = {45, 55, 77, 88}
S3.pop()
print(S3)

# discard (delete an element if it`s on the set)
S4 = {99, 15, 27, 98}
S4.discard(99)
print(S4)

# remove (delete an element if it`s on the set)
# if not throws exception
S5 = {33, 22, 11}
S5.remove(33)
print(S5)

S.remove((102, 103))
print(S)

# clear (remove all elements on the set)
S5.clear()
print(S5)
