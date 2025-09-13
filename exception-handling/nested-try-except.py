L = [100, 200, 300, 400, 500]

try:
    try:
        index = int(input('Enter an index: '))
    except ValueError as e:
        print(e)

    print(L[index])
except IndexError as e:
    print(e)

except Exception as e:
    print(e)
