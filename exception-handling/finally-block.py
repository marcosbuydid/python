def func():
    try:
        x = int('264')
    except Exception as e:
        raise e
    else:
        return x
    # if finally is not placed here, print function
    # is unreachable
    # raise keyword is used to trigger (or raise)
    # an exception, either built-in or custom,
    # during the execution of a program.
    finally:
        print('End Func')


def func1():
    try:
        y = int('abc')
    except Exception as e:
        raise e
    else:
        return y
    finally:
        print('End Func1')


result = func()
print(result)  # prints End and 264 line below

# here you can see that besides an exception is thrown
# finally block is executed anyway.
result1 = func1()
print(result1)
