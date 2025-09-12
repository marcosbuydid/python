a = 20
b = 4
c = 0

try:
    result = a // c
    print(result)
except:
    print('Cannot divide by zero')

print('End')

L = [10, 20, 30, 40, 50]
try:
    index = 3
    print('The value associated to the index is:', L[index])
except:
    print('Invalid index')
print('End')
