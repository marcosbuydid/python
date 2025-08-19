# the yield keyword is used to return a list of values from a function.
# unlike the return keyword which stops further execution of the function,
# the yield keyword continues to the end of it.
# when you call a function with yield keyword(s), the return value will be
# a list of values, one for each yield.

def flatten_list(L):
    for element in L:
        if hasattr(element, '__iter__'):
            yield from flatten_list(element)
        else:
            yield element


L = [[10, 22, [13, 43, [52, 36, 78], 87], 94, [109, 121]]]

flat = flatten_list(L)
flat_list = list(flat)
print(flat_list)
