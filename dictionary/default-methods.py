dictionary = {100: 'One Hundred', 200: 'Two Hundred', 300: 'Three Hundred', 400: 'Four Hundred'}

# update
d1 = {500: 'Five Hundred'}
dictionary.update(d1)
print(dictionary)

# from keys
k1 = [1, 2, 3, 4]
dictionary_1 = dict.fromkeys(k1)
print(dictionary_1)  # {1: None, 2: None, 3: None, 4: None}

# copy
# will create a shallow copy
# dictionary_2 is not the same as dictionary
# is another dictionary containing the same elements
dictionary_2 = dictionary.copy()

# pop
dictionary_2.pop(500)
print(dictionary_2)

# define alternate output if value is not
# present on the dictionary to avoid key error
print(dictionary_2.pop(8000, 'Not found'))

# popitem
dictionary_2.popitem()
print(dictionary_2)

# clear
dictionary_2.clear()
