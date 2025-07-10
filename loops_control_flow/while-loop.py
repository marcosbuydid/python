# sum digits of a number
n = 12345
result = 0
while n > 0:
    r = n % 10
    result = result + r
    n = n // 10
print('the sum of digits is: ', result)

# reverse a number
l = 45678
m = 45678
reverse = ''
while m > 0:
    r = m % 10
    reverse = reverse + str(r)
    m = m // 10
print(l, 'reversed is:', int(reverse))

# reverse a number other version
l1 = 78953
m1 = 78953
reverse1 = 0
while m1 > 0:
    r = m1 % 10
    reverse1 = reverse1 * 10 + r
    m1 = m1 // 10
print(l1, 'reversed is:', int(reverse1))

# check if a number is palindrome
a = 1221
b = a
rev_result = 0
while a > 0:
    r = a % 10
    rev_result = rev_result * 10 + r
    a = a // 10
if rev_result == b:
    print(b, rev_result, 'are palindrome')
else:
    print(b, rev_result, 'are not palindrome')

# sum of N numbers
number = 15
index = 0
sum_result = 0
while index < number:
    index = index + 1
    sum_result = sum_result + index
print('the sum of', number, 'is:', sum_result)
