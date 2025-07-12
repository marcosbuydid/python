# tells if a string contains only
# alphabet chars
s = 'Summer'
result = s.isalpha()
print(result)

# returns true if a string is lowercase
result1 = s.islower()
print(result1)

# returns true if a string is uppercase
result2 = s.isupper()
print(result2)

# returns true if a string begins with
# uppercase
result3 = s.istitle()
print(result3)

# returns true if a string contains only
# whitespaces
result4 = s.isspace()
print(result4)

# returns true if all chars of a string
# are printable
result5 = s.isprintable()
print(result5)

# returns true if a string is a valid
# python identifier
result6 = s.isidentifier()
print(result6)

# returns true if a string contains
# only digits
s1 = '1234'
result7 = s1.isdigit()
print(result7)

# returns true if a string is decimal
s2 = '12348'
result8 = s2.isdecimal()
print(result8)

# returns true if a string is numeric
s3 = '12348a'
result9 = s3.isnumeric()
print(result9)

# return true if all chars in a string are ASCII
result10 = s3.isascii()
print(result10)

# return true if a string is alphanumeric
result11 = s3.isalnum()
print(result11)
