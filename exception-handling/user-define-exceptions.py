class NegativeError(Exception):
    # constructor
    def __init__(self):
        self.msg = 'Dimensions cannot be negative'

    def __str__(self):
        return self.msg


def area_calculator(length, width):
    if length > 0 and width > 0:
        area = length * width
        return area
    else:
        raise NegativeError()


result = area_calculator(-100, 100)
print(result)
