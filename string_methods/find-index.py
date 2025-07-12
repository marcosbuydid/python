# index of lowest substring found in a string
# -1 if not found
s = 'Hello Clari how are you'
index = s.find('i')
print(index)

# index of lowest substring found in a string
# from specific position
s1 = 'This is amazing'
index1 = s1.find('i', 4)
print(index1)

# index of lowest substring found in a string
# from specific range position
s2 = 'You are welcome'
index2 = s2.find('i', 4, 8)
print(index2)

# index of highest substring found in a string
s3 = 'This is an amazing work'
index3 = s3.rfind('w')
print(index3)

# index of lowest substring found in a string
# throws value error when not found
s4 = 'Book that trip'
index4 = s4.index('p')
print(index4)

# index of highest substring found in a string
# throws value error when not found
s5 = 'Thank you'
index5 = s5.rindex('u')
print(index5)
