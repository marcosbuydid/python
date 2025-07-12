# make the first char of a string uppercase
s = 'today is friday'
result = s.capitalize()
print(result)

# make all chars of a string uppercase
result1 = s.upper()
print(result1)

# make all chars of a string lowercase
s1 = 'TODAY IS FRIDAY'
result2 = s1.lower()
print(result2)

# start with uppercase every word of
# a string
result3 = s.title()
print(result3)

# convert to uppercase chars that are lowercase
# and vice versa
s2 = 'I like Saturdays'
result4 = s2.swapcase()
print(result4)

# return a string for a caseless comparison
result5 = s2.casefold()
print(result5)
