# gives the type of object
print(type(10))
print(type(3.15))
print(type('Hello'))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({'a': 1}))

# check if an object belong to its class
x = 10
print(isinstance(x, int))
print(isinstance(x, float))
print(isinstance(x, (int, float)))
print(isinstance('Python', (int, str)))

# check if an object has a method or not,
# or member or not
text = 'Silvina'
print(hasattr(text, 'lower'))
print(hasattr(text, 'search'))
print(hasattr(text, 'find'))

# if a class or module is having some members, it
# will give you the reference to that one
import math

print(getattr(math, 'pi'))
print(getattr(math, 'sqrt')(25))

# gives the id of an object
x = 18
y = 29
print(id(x))
print(id(y))
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(id(l1))
print(id(l2))

# gives all the methods of a class members of a class
# and if it is a module, it gives you all
print(dir(list))
print(dir(math))

# Return the canonical string representation of the object
print(repr('jupiter'))
