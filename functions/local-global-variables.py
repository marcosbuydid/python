# global variables declared outside of functions
# can be read inside any function
# local variables declared inside a function
# must be declared before function call

v = 4.19
print('Outside-1', v)


def function():
    a = 13
    # modifying v value inside function
    # will only have scope inside it.
    v = 80.0
    print('local variable:', a)
    print('global variable:', v)


function()
print('Outside-2', v)

# locals() gives a dictionary of local variables
# globals() gives a dictionary of global variables
x, y, z = 4, 1.23, 'Hello'


def function_1():
    a, b, c = 1, 2, 3
    print(locals())
    print(globals())


function_1()
