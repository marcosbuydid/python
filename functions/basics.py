def volume_calculator(length, width, height):
    return length * width * height


print(volume_calculator(10, 20, 30))


# positional vs keyword arguments

def power_calculator(voltage, current):
    return voltage * current


# first parameter corresponds to voltage
# and second to current.
# based on their position arguments are passed.
print(power_calculator(2, 3))

# now parameters are explicit defined but not
# based on their position but their values.
# they are called keyword arguments.
print(power_calculator(current=4, voltage=10))

# mixed arguments
# either positional or keyword but not both.
# positional on left, keyword on right.
print(power_calculator(10, current=4))


# if you want to make an argument as default in the function
# you set a default value
def volume_calculator2(length, width, height=3):
    return length * width * height


# then, when calling the function, the default argument
# is omitted.
print(volume_calculator2(15, 20))


# to define all positional arguments in a function call
# the / is used at the end of the parameters.
def volume_calculator3(length, width, height, /):
    return length * width * height


# to define some positional arguments in a function call
# the / is used between the positional and non-positional ones.
def volume_calculator4(length, /, width, height):
    return length * width * height


# keyword-only arguments

# to define which ones are positional or keyword only in a function call,
# the * is used. to the left of it goes positional or keyword
# and to the right the keyword-only ones.
def volume_calculator5(length, *, width, height):
    return length * width * height


# if all arguments need to be keyword-only the * goes first
# before all the arguments in the function call.
def volume_calculator6(*, length, width, height):
    return length * width * height


# positional-only and keyword-only arguments mixed
def custom_func(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


custom_func(1, 2, 3, d=4, e=5, f=6)


# variable length positional arguments
# in order to define on a function call
# an argument only with an * is used
def custom_func_1(*args):
    print(args)


custom_func_1(5)
custom_func_1(9, 10, "Hello")
custom_func_1("Python", 9 + 15j, 3.13)


# tuple is created for variable length arguments
# a and b must be passed as positional only arguments
def custom_func_2(a, b, *args):
    print(a, b, args)


custom_func_2(100, 200, 4, 5)


# a and b must be passed as keyword only arguments
def custom_func_3(*args, a, b):
    print(a, b, args)


custom_func_3(100, a=40, b=50)
