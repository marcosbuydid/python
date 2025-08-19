# iter (iterable) gives an iterator on iterable
# next (iterator) gives an element and moves next

L1 = [125, 234, 384]
it = iter(L1)
print(next(it))

T1 = (40, 50, 60)
it1 = iter(T1)
print(next(it1))

S1 = {70, 44, 50}
it2 = iter(S1)
print(next(it2))

s1 = 'Python'
it3 = iter(s1)
print(next(it3))

r = range(13, 100)
it4 = iter(r)
print(next(it4))

# generators

def myrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

m = myrange(13)
print(next(m))

def days():
    d1 = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    i = 0
    while True:
        yield d1[i]
        i = (i + 1) % 7

d = days()
print(next(d))


