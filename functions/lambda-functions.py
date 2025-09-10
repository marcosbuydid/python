def double(x):
    return x * 2


# equivalent lambda function
k = lambda x: x * 2

print(double(34))
print(k(34))

a = lambda b, c: b + c
print(a(10, 20))

print((lambda e: e * 2)(7))

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(lambda x: x % 3 == 0, l1)
l2 = list(f)
print(l2)  # [3, 6, 9]

l2 = [9, 8, 7]
l3 = list(map(lambda x: -x, l2))
print(l3)  # [-9, -8, -7]

l4 = [10, 11, 12, 13, 14, 15, 16, 17, 18]
g = lambda x: x if x % 2 == 0 else -x

l5 = list(map(g, l4))
print(l5)

l6 = [[6, 2, 'Eight'], [1, 9, 'Ten'], [3, 1, 'Four']]
l6 = sorted(l6, key=lambda x: x[0] + x[1])
print(l6)  # [[3, 1, 'Four'], [6, 2, 'Eight'], [1, 9, 'Ten']]
