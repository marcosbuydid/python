# functions
a = 12.69
b = True
s1 = '125'
s2 = '0b1010'
s3 = '0xB'

x = int(a)
print(x, type(x))

print(int(b))

print(int(s1))

x = int(s2, 2)
print(x, type(x))

c = 10
d = -15
e = -2.4e-3
f = 4 + 4j
g = False

x = bool(c)
print(x, type(x))
print(bool(d))
print(bool(e))

h = -15.4
y = complex(h)
print(y, type(y))

print(complex(g))  # Oj
print(complex(f))

i = 30
z = str(i)
print(z, type(z))

j = -1.2E3
k = str(j)
print(k)

l = str(b)
print(l)

m = str(f)
print(m)
