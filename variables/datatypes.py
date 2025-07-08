import sys

# numeric datatypes

# int & float
a = 202
b = 1234567890123456789

# memory size needed to store that variables
print(sys.getsizeof(a))  # 28 bytes
print(sys.getsizeof(b))  # 36 bytes

# if we assign a new value for variable "a", python will assign
# a new memory location for the new value because it does not know
# what is the size of the data you are assigning and how much memory
# it requires.
print(id(a))
a = 405
print(id(a))

c = 24.70
d = -2.54
e = -3.5E2
f = 9.4e-2
print(c, d, e, f)

# bool & complex
g = True
h = False
print(g, h)
print(c > d)  # True

k = 9 + 5j
print(type(k))

k = complex(5, 3.7)
print(k)

l = complex(10)
print(l)  # no imaginary part (0j)

# literals or constants
m = 303
n = 34_56_32_90
print(m, n)

l = 32E2
o = 14.5e-2
print(o, l)

name = 'Venus'
name1 = "Venus"
name2 = "'Venus'"
print(name, name1, name2)

## integer literals
p = 10  # decimal
q = 0b1010  # binary
r = 0o12  # octal
s = 0xA  # hexadecimal
print(p, q, r, s)
