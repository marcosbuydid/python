file = open('props.txt', 'r')
print(type(file))

data = file.readline()
print(data)
file.close()

file1 = open('props.txt', 'w')
lst = ['One\n', 'Two\n', 'Three\n', 'Four\n']
file1.writelines(lst)
file1.close()

with open('props.txt', 'r') as file2:
    data = file2.read()
    print(data)