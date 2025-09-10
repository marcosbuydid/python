def external(msg):
    def greetings():
        print('*' * 15)
        print(msg)
        print('*' * 15)

    return greetings


function = external('Welcome Marcos')
function()


def get_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c1 = get_counter()
c2 = get_counter()

print(c1(), c1(), c1())  # 1 2 3
print(c2(), c2(), c2())  # 1 2 3
