def function(n):
    if n > 0:
        print(n, end=" ")
        function(n - 1)


function(10)


# factorial of n numbers
def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)

print('\n',factorial(5))
