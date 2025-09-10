def decorator(f):
    def internal():
        print('+' * 15)
        f()
        print('+' * 15)

    return internal


@decorator
def display():
    print('Welcome')


display()
