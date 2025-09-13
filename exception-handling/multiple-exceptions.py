L = [100, 250, 340, 470, 508]
try:
    index = 3
    print('The value associated to the index is:', L[index])
except (IndexError, TypeError) as err:
    print(err)
except Exception as err:
    print(err)
print('End')
