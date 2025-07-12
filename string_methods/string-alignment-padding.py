# return a left-justified string of length width.
# padding is done using the specified fill character (default is a space)
s = 'Guitar'
result = s.ljust(7, '*')
print(result)

# return a right-justified string of length width.
# padding is done using the specified fill character (default is a space)
s1 = 'Bass'
result1 = s1.rjust(7, '*')
print(result1)

# return a centered string of length width.
# padding is done using the specified fill character (default is a space)
s2 = 'Drums'
result2 = s2.center(7, '*')
print(result2)

# return a new string with specific char removed
s3 = '$$$Cello'
result3 = s3.lstrip('$')
print(result3)

# return a new string with specific char removed
s4 = '$$$Cello'
result4 = s4.rstrip('o')
print(result4)

# remove specified chars from a string
s5 = '$$$Trumpet   !! *'
result5 = s5.strip('$! *')
print(result5)
