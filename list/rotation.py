l = [1, 2, 3, 4, 5]
rotation = 3
result = []

if rotation > len(l):
    print('rotation number must be less than length of list')
else:
    for j in l[rotation: len(l)]:
        result.append(j)

    for i in l[0:rotation]:
        result.append(i)
    print(result)
