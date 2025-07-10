sum_result = 0
for i in range(5):
    sum_result = sum_result + i
print(sum_result)

s1 = 'aei'
for x in s1:
    print(x)

# factorial of a given number
number = 5
result = 1
for i in range(1, number + 1):
    result = result * i
print(result)

# fibonacci series
num = 30
a = 0
b = 1
for i in range(0, num):
    c = a + b
    a = b
    b = c
print(a)

# check if a number is prime
number_input = 11
factors_qty = 0
for i in range(1, number_input + 1):
    if number_input % i == 0:
        factors_qty += 1
if factors_qty == 2:
    print(number_input, 'is a prime number')
else:
    print(number_input, 'is not a prime number')
