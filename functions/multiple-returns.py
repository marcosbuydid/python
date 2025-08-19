# a function can have multiple returns in python

def function(a, b, c):
    addition = a + b + c
    product = a * b * c
    return addition, product


print(function(1, 2, 10))


def grade_calculator(cal1, cal2, cal3):
    addition = cal1 + cal2 + cal3
    average = addition / 3
    if average > 45:
        grade = 'Pass'
    else:
        grade = 'Fail'
    return addition, average, grade


print(grade_calculator(40, 55, 50))
print(grade_calculator(20, 15, 30))

