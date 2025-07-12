s = 'Python is a programming language'
result = s.startswith('Python')
print(result)

result1 = s.endswith('programming')
print(result1)

# remove the prefix of a string
s2 = 'AI is changing the world'
result2 = s2.removeprefix('AI')
print(result2)

# remove the suffix of a string
result3 = s2.removesuffix('world')
print(result3)

# partition the string into three parts
# using a separator
result4 = s2.partition('is')
print(result4)

# partition the string into three parts
# using a separator
result5 = s2.rpartition('s')
print(result5)
