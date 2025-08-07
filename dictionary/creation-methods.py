# using iterable pairs
dictionary = dict([(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')])

# using zip function
L1 = [1, 2, 3, 4]
L2 = ['One', 'Two', 'Three', 'Four']
dictionary_1 = dict(zip(L1, L2))

# using enumerate function
L3 = ['One', 'Two', 'Three', 'Four']
dictionary_2 = dict(enumerate(L3, start=100))
