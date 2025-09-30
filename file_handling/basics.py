file = open('data.txt', 'r')
str1 = file.read(10)
print(str1)
# str2 continues at the next position
# of str1 pointer was
str2 = file.read()
print(str2)
file.close()

# modes of opening a file
# r to read data from file
# w to write dats from file
# a to append data to the file
# r+ to read and write data of a file
# w+ to write and read data into a file
# a+ to append and read data of a file
# x to open the file in exclusive creation mode

file1 = open('modes.txt', 'w')
file1.write('Writing a file in python')
file1.close()
file2 = open('modes.txt', 'r')
str2 = file2.read()
print(str2)
file2.close()
