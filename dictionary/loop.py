dictionary = {1: 'One', 2: 'Two', 3: 'Three'}

# get dictionary keys
dictionary.keys()

for a in dictionary.keys():
    print(a)

# get dictionary values
dictionary.values()

for b in dictionary.values():
    print(b)

# get dictionary items
dictionary.items()

for c, d in dictionary.items():
    print(c, d)

# using get to get specific value
print(dictionary.get(3))

# set default output if the value is not
# on the dictionary
print(dictionary.get(4, 'Undefined'))

# if the key is already present in the dictionary, setdefault() returns
# the existing value associated with that key.

# if the key is not found in the dictionary, setdefault() inserts the key
# into the dictionary with the specified default_value and then returns
# the default_value. If default_value is not provided, defaults it sets to None.
print(dictionary.setdefault(100))
