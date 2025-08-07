# how to invert a dictionary
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

inverted = {}

for key, value in original.items():
    if value not in inverted:
        inverted[value] = key
    else:
        inverted[value].add(key)

print("Inverted Dictionary:", inverted)
