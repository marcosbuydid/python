dictionary = {1: 'One', 2: 'Two', 3: 'Three'}
print(dictionary)

# read
print(dictionary[1])  # One

# update
dictionary[3] = 'New value'
print(dictionary)

# write
dictionary[4] = 'Four'
print(dictionary)

# traverse
for i in dictionary:
    print(i, dictionary[i], end=" ")

# more examples
# keys can be of any type
dictionary_1 = {1: 3.5, 2.9: True, 5 + 9j: 'cde'}

dictionary_2 = {1: [10, 11], 2: (2, 7), 3: {9, 10}, 4: {1: 1, 2: 2}}
