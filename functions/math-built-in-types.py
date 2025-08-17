# absolute value of a number
print(abs(-90.12))
print(abs(3 + 4j))

# power function of a number
print(pow(10, 2))  # 10 x 10
print(pow(10, -2))
print(pow(10, 2, 3))  # 10 x 10 % 3 = 1

# round function of a number
print(round(3.14))
print(round(-783.64))
# rounding with specified decimal places
print(round(4564.798894, 3))

# modulus function of a number
print(divmod(34, 2))

# minimum function that return the minimum
# in a group of numbers
print(min(-100, -120, 1, 45, 67))
print(min(-1.0091, 10091, -2.983435))
print(min(-1.0091, 10091, -2.983435, key=abs))
print(min([], default="Empty list"))

# max function
words = ['apple', 'banana', 'orange', 'lemon', 'pineapple']
print(max(words, key=len))

# sum function
print(sum([1, 2, 3, 4, 5, 6]))

# eval function
print(eval("10 + 20 * 4 - 5"))  # 85
print(eval("10 + 60 * 4 - 5 % 4 * 2 - 9"))

globals_dict = {"x": 67, "y": 43}
locals_dict = {"z": 27}
print(eval("x + y + z", globals_dict, locals_dict))
