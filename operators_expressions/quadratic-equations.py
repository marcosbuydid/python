import math

a = 1
b = -5
c = 6

root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print('the roots of the quadratic equation are:', root1, root2)