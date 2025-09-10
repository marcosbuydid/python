def external():
    def internal():
        print('internal function')

    print('external function')
    internal()


external()  # output: external function then internal function


# area of a rectangular prismatic object
def prismatic_rectangle_area(length, base, height):
    def area(d1, d2):
        return d1 * d2

    return 2 * (area(length, base) +
                area(base, height) +
                area(length, height))


print("Area is:", prismatic_rectangle_area(10, 5, 2))
