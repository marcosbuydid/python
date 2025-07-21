import random as rd

l = [45, 53, 21, 23, 78, 98, 55, 11, 90]

rd.shuffle(l)
print(l)

# k represent the random number of elements to choose
l1 = rd.choices(l, k=4)
print(l1)
