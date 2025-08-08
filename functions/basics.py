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
print(power_calculator(current=4, voltage=10))

# mixed arguments
# either positional or keyword but not both.
# positional on left, keyword on right.
print(power_calculator(10, current=4))
