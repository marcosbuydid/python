# traverse a string
s = 'Hello world'
for letter in s:
    print(letter, end=' ')

# slicing
s1 = 'Hello Clari'
print(s1[5:11])  # output Clari

# slicing a string in reverse
s2 = 'Hello Clari'
print(s2[::-1])  # output iralC olleH

# slicing a string in reverse partial
s3 = 'Hello Clari'
print(s3[11:5:-1])  # output iralC

# check if a substring is in a string
s4 = 'Travel to Japan'
print('vel' in s4)
