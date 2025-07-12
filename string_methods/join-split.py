# replace a substring in a string
s = 'H*e*l*l*o'
result = s.replace('*', '-')
print(result)

# replace a substring in a string with
# a quantity specified
s1 = 'H*e*l*l*o'
result1 = s1.replace('*', '-', 2)
print(result1)

# join two strings
s2 = 'abc'
s3 = 'def'
result2 = s2.join(s3)
print(result2)  # output dabceabcf

# split a string using a char
s4 = 'Believe me'
result3 = s4.split(' ')
print(result3)
