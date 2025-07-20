l = [3, 5, 6, 3, 7, 8, 1, 4, 5, 9, 6]
result = []
for i in l:
    if i not in result:
        result.append(i)
print(result)
