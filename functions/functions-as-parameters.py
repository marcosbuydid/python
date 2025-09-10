def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def arithmetic(f, a, b):
    return f(a, b)


add = arithmetic(addition, 2, 3)
diff = arithmetic(subtraction, 5, 7)
print(add, diff)
